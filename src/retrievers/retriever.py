from langchain_qdrant import QdrantVectorStore
from src.vectordb.qdrant_store import vector_store 
from src.config import TOP_K


retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": TOP_K}
        )


