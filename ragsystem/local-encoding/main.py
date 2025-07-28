import os
import threading
import asyncio
from langchain_ollama import ChatOllama
import readline
from fastmcp import Client
import torch

from server import start_mcp_server
def query_ollama_model(query: str, model_name = "llama3.2:3b"):
    """
    Queries the Hugging Face model and returns the response.
    """
    llm = ChatOllama(model=model_name, base_url="http://localhost:11434", temperature=0)
    response = llm.invoke(input=query)
    print(response.content)


async def logic_loop(mcp_client: Client, local_model="llama3.2:3b"):
    """
    Continuously prompts the user for a question and retrieves the relevant passage from the database.
    """
    while True:
        print(torch.__version__)
        model_name = local_model
        query = await asyncio.to_thread(
            input,
            f"> Enter your question to retrieve a document using {model_name},\n"
            "> To query Gemini 2.5 Flash with this question and document, add an exclamation point '! [query]'\n"
            "> To exit, type 'exit':\n> "
        )
        if query.lower() == 'exit':
            break
        elif query.startswith('!'):
            query_ollama_model(query.strip("!"))
        else:
            relevant_passage = await mcp_client.call_tool('get_relevant_passage_tool', {'query': query})
            print(f"Relevant passage: \n{relevant_passage.content}")


#start server
# Settings:
chosen_model = "text-embedding-004"
chroma_dir = os.path.dirname(__file__) + "/chroma_db"
documents_dir = os.path.dirname(os.path.dirname(__file__)) + "/documents" # Adjusted to point to the parent directory's documents folder


def start_mcp_server_in_background(chroma_dir, documents_dir, chosen_model):
    """
    Ensures the database setup is complete before starting the MCP server in a background thread.
    """
    # Perform synchronous database setup
    print("Setting up the database...")
    server = start_mcp_server(chroma_dir, documents_dir)
    print("Database setup complete.")

    # Start the server in a background thread
    def run_server():
        server.run(host="0.0.0.0", port=8000, transport="streamable-http")

    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    print("MCP server is running in the background.")


async def main():
    start_mcp_server_in_background(chroma_dir, documents_dir, chosen_model)
    await asyncio.sleep(5)  # wait a moment for the server to start
    async with Client(
        "http://localhost:8000/mcp",
        #transport="streamable-http"
    ) as mcp_client:
    # wait a moment for the server to start
        await asyncio.sleep(1)
        await logic_loop(mcp_client)
if __name__ == "__main__":
    asyncio.run(main())