import sys
import os
import chromadb
from pathlib import Path
import hashlib
import readline
from embeddingModels import HFEmbeddingFunction, all_MiniLM_L6_v2
from chromadb import Documents, EmbeddingFunction, Embeddings
import tiktoken
from mcp.server.fastmcp import FastMCP

import uvicorn
from uvicorn.config import LOGGING_CONFIG
from starlette.applications import Starlette
from starlette.routing import ( Route, Mount )

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware import Middleware
from starlette.responses import JSONResponse
from starlette.requests import Request

# The expected API key value for authentication
API_KEY = "super_secret_value"
HEADER = "X-API-Key"
MCP_PREFIX = "/"

class ApiKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith(MCP_PREFIX):
            supplied = request.headers.get(HEADER)
            if supplied != API_KEY:
                return JSONResponse(
                    {"detail": "Invalid API key"},
                    status_code=401
                )
        return await call_next(request)

middleware = [ Middleware(ApiKeyMiddleware) ]

def create_chroma_db(documents, metadatas, name, chroma_dir, hf_embedding=all_MiniLM_L6_v2):
    from chromadb.config import Settings

    chroma_client = chromadb.PersistentClient(
        path=chroma_dir
    )

    db = chroma_client.get_or_create_collection(
        name=name,
        embedding_function=HFEmbeddingFunction(hf_embedding)
    )

    for doc, meta in zip(documents, metadatas):
        doc_id = hash_doc(doc, meta)
        
        # Check if the ID already exists in the DB
        if not db.get(ids=[doc_id])["ids"]:
            db.add(documents=[doc], ids=[doc_id], metadatas=[meta])  # embedding happens here

    return db

def find_all_files(root_dir):
    return [str(path) for path in Path(root_dir).rglob('*') if path.is_file()]

def hash_doc(doc: str, metadata: dict) -> str:
    """
    Generate a unique hash for a document based on its content and metadata.
    """
    combined = doc + str(metadata)
    return hashlib.sha256(combined.encode('utf-8')).hexdigest()

def get_relevant_passage(query, db, results=1):
        passage = db.query(query_texts=[query], n_results=results)['documents'][0][0]
        return passage

def split_text_with_tiktoken(text, chunk_size=512, chunk_overlap=100):
    """
    Splits text into chunks using TikToken with a specified chunk size and overlap.
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)

    chunks = []
    for i in range(0, len(tokens), chunk_size - chunk_overlap):
        chunk_tokens = tokens[i:i + chunk_size]
        chunks.append(encoding.decode(chunk_tokens))

    return chunks

def start_mcp_server(chroma_dir, documents_dir):
    # Setup the documents
    if not os.path.exists(chroma_dir):
        a = input(f"The chroma directory {chroma_dir} does not exist. Do you want to create it? (y/n): ")
        if a.lower() != 'y':
            print("Exiting the program.")
            exit(1)
        os.makedirs(chroma_dir)

    # Setup documents to embed
    paths = find_all_files(documents_dir)
    if not paths:
        print("No markdown files found in the documents directory.")
        exit(1)
    documents = []
    metadatas = []

    for path in paths:
        with open(path, 'r') as f:
            contents = f.read()
        # LOCATION TO ADD MORE METADATA!!
        if contents.strip():
            # Title could be the filename or extracted from the first Markdown heading
            fileTitle = Path(path).stem  # e.g., "xrootd_config" from "xrootd_config.md"
            # Optionally extract from content: e.g., first line that starts with '# '
            title = ""
            for line in contents.splitlines():
                if line.strip().startswith("# "):
                    title = line.strip("# ").strip()
                    break

            # Split the document into chunks using TikToken
            chunks = split_text_with_tiktoken(contents)
            for chunk in chunks:
                documents.append(chunk)
                metadatas.append({"document_title": title, "file_title": fileTitle})

    if len(documents) == 0:
        print("No documents found to embed.")
        exit(1)

    # Ensure the chroma_dir exists
    if not os.path.exists(chroma_dir):
        os.makedirs(chroma_dir)

    # Start the vector database
    db = create_chroma_db(
        documents=documents,
        name="xrd_test",
        metadatas=metadatas,
        chroma_dir=chroma_dir,
        hf_embedding=all_MiniLM_L6_v2
    )

    # Start the MCP server
    server = FastMCP()

    @server.tool()
    def get_relevant_passage_tool(query: str, results: int = 1) -> str:
        '''
        Tool to retrieve relevant passage from the database on Xrootd. Change results to get more than one passage. 
        '''
        print(f"Received query: {query}, for tool: get_relevant_passage_tool")
        passage = get_relevant_passage(query, db, results=results)
        return passage if passage else "No relevant passage found."

    @server.tool()
    def retrieve_document_file(file: str) -> str:
        '''
        Tool to retrieve the full content of a document file by its file name.
        '''
        print(f"Received request for file: {file}, for tool: retrieve_document_file")
        for path in paths:
            if file in path:
                with open(path, 'r') as f:
                    return f.read()
        return f"No document found with file name: {file}"
	
    return server



if __name__ == "__main__":
    chroma_dir = os.path.dirname(__file__) + "/chroma_db"
    documents_dir = os.path.dirname(__file__) + "/documents" # Adjusted to point to the parent directory's documents folder

    server = start_mcp_server(chroma_dir, documents_dir)

    arguments = sys.argv
    print("Arguments passed to the script:", arguments)
    if "--stdio" in arguments:
        server.run(transport="stdio")
    else:
        app = Starlette(routes=[Mount("/", app=server.streamable_http_app())], middleware=middleware,
                lifespan=lambda xyz: server.session_manager.run())
        LOGGING_CONFIG["formatters"]["access"]["fmt"] = \
            "%(asctime)s %(levelname)s %(client_addr)s - %(request_line)s %(status_code)s"
        uvicorn.run(app,
                    host="0.0.0.0",
                    port=8000,
                    #ssl_certfile="./hostcert.pem",
                    #ssl_keyfile="./hostkey.pem",
                    headers=[("server", "")],
                    timeout_graceful_shutdown=10)
    # https://localhost:8000/mcp/ when ssl_certfile and ssl_keyfile are provided





