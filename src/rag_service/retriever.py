from src.utils.config import TOP_K
from src.rag_service.qdrant_store import get_qdrant_client,ensure_faq_collection
from src.rag_service.hf_embedding import Embeddings
import uuid
from qdrant_client import models

class VectorStore:
    def __init__(self):
        self.collection_name = "documents"
        self.client = get_qdrant_client()
        self.embeddings = Embeddings()
 
    async def initialize(self):
        await ensure_faq_collection()
    
    async def add_documents(self, chunks):

        points = []

        for idx, chunk in enumerate(chunks):

            vector = self.embeddings.embed_query(
                chunk.page_content
            )

            points.append(
                models.PointStruct(
                    id=str(uuid.uuid4()),
                    vector=vector,
                    payload={
                        "content": chunk.page_content,
                        "source_file": chunk.metadata.get(
                            "source_file"
                        ),
                        "page": chunk.metadata.get("page"),
                    },
                )
            )

        await self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )
 
    async def vector_search(self, query: str, top_k: int = TOP_K) -> list[dict]:
        """Search the vector store and return results with scores.
 
        Args:
            query: The search query string.
            top_k: Number of top results to return.
 
        Returns:
            A list of dicts, each containing 'content', 'source_file', and 'score'.
        """
        query_vector = await self.embeddings.aembed_query(query)
 
        results = await self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=top_k,
        )
 
        return [
            {
                "content": hit.payload.get("content", ""),
                "source_file": hit.payload.get("source_file", "unknown"),
                "score": hit.score,
            }
            for hit in results.points
        ]