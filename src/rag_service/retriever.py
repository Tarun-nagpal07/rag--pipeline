from langchain_qdrant import QdrantVectorStore
from src.rag_service.qdrant_store import VectorStore 
from src.utils.config import TOP_K
from src.utils.errors import RetrievalError



def Retriever():
    try:
        vector_store = VectorStore() 
        retriever = vector_store.as_retriever(
                search_type="mmr",
                search_kwargs={"k": TOP_K}
        )
        return retriever
    except Exception as e:
        raise RetrievalError(str(e))
    




