from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from src.embeddings.hf_embedding import embeddings
from src.utils.config import QDRANT_HOST

client = QdrantClient(
    url=QDRANT_HOST
)

vector_store = QdrantVectorStore(
    client=client,
    collection_name="documents",
    embedding=embeddings
)