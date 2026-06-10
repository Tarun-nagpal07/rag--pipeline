from langchain_qdrant import QdrantVectorStore
from src.rag_service.qdrant_store import VectorStore 
from src.utils.config import TOP_K
from src.utils.errors import RetrievalError



def Retriever():
    try:
        vector_store = VectorStore() 
        retriever = vector_store.as_retriever(
            search_type='mmr',
            search_kwargs={'k':TOP_K}
        )
        return retriever
    except Exception as e:
        raise RetrievalError(str(e))


# results = vector_store.similarity_search_with_score(
#                 query,
#                 k= TOP_K


#         )
#         docs = []

#         for doc, score in results:
#             doc.metadata["score"] = score
#             docs.append(doc)
#         print(doc)





# import os
# from dotenv import load_dotenv
# from app.db.qdrant import get_qdrant_client, ensure_faq_collection
# from app.services.llm import get_embeddings
 
# load_dotenv()
 
# class VectorStore:
#     def __init__(self):
#         self.collection_name = "ecommerce-knowledge"
#         self.client = get_qdrant_client()
#         self.embeddings = get_embeddings()
 
#     async def initialize(self):
#         await ensure_faq_collection()
 
#     async def vector_search(self, query: str, top_k: int = 3) -> list[dict]:
#         """Search the vector store and return results with scores.
 
#         Args:
#             query: The search query string.
#             top_k: Number of top results to return.
 
#         Returns:
#             A list of dicts, each containing 'content', 'source_file', and 'score'.
#         """
#         query_vector = await self.embeddings.aembed_query(query)
 
#         results = await self.client.query_points(
#             collection_name=self.collection_name,
#             query=query_vector,
#             limit=top_k,
#         )
 
#         return [
#             {
#                 "content": hit.payload.get("content", ""),
#                 "source_file": hit.payload.get("source_file", "unknown"),
#                 "score": hit.score,
#             }
#             for hit in results.points
#         ]