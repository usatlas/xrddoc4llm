from langchain_huggingface import HuggingFaceEmbeddings
from chromadb.utils.embedding_functions import EmbeddingFunction
from typing import List


class HFEmbeddingFunction(EmbeddingFunction[List[str]]):
    def __init__(self, hf: HuggingFaceEmbeddings):
        self.hf = hf
    def __call__(self, input: List[str]):
        # Might need to call embed_documents for batches
        return self.hf.embed_documents(input)
    def name(self):
        # Return a unique name for this embedding function
        return "HuggingFaceEmbeddingFunction"

qwen3_embedding_4B = HuggingFaceEmbeddings(
    model_name="Qwen/Qwen3-Embedding-4B",
    model_kwargs={"device": "cpu"},

all_MiniLM_L6_v2 = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
)
