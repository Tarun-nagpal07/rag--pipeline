import os
from functools import lru_cache
from qdrant_client import AsyncQdrantClient, models
from qdrant_client.models import VectorParams, Distance, PayloadSchemaType
from src.utils.config import QDRANT_API,QDRANT_URL
 
@lru_cache(maxsize=1)
def get_qdrant_client() -> AsyncQdrantClient:
    """Return a singleton AsyncQdrantClient."""
    qdrant_url = QDRANT_URL
    qdrant_api_key = QDRANT_API
    return AsyncQdrantClient(url=qdrant_url, api_key=qdrant_api_key, timeout=30)
 
 
async def ensure_faq_collection():
    """Ensure the FAQ knowledge collection exists."""
    client = get_qdrant_client()
    collection_name = "documents"
    if not await client.collection_exists(collection_name):
        await client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=768, distance=Distance.COSINE),
        )
 
