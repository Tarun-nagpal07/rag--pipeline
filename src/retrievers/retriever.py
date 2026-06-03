from langchain_qdrant import QdrantVectorStore
from src.vectordb.qdrant_store import vector_store 
from src.utils.config import TOP_K
from src.utils.errors import RetrievalError

retriever = vector_store.as_retriever(
                search_type="mmr",
                search_kwargs={"k": TOP_K}
)


