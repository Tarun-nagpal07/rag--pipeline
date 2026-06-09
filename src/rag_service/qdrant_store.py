from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from src.rag_service.hf_embedding import Embeddings
from src.utils.config import QDRANT_HOST
from src.utils.errors import VectorStoreError

client = QdrantClient(
    url=QDRANT_HOST
)

def VectorStore():
    try:
        vector_store = QdrantVectorStore(
            client=client,
            collection_name="documents",
            embedding=Embeddings(),
            
        )
        return vector_store
    except Exception as e:
        raise VectorStoreError(str(e))

