from src.utils.logger import get_logger
from src.rag_service.retriever import VectorStore
logger = get_logger(__name__)

async def retrieve_from_doc(question: str) -> list[dict]:
    """
    Search and return relevant health-related information from Qdrant.

    Returns:
        [
            {
                "content": "...",
                "source_file": "...",
                "score": 0.82,
            }
        ]
    """
    vector_store = VectorStore()

    results = await vector_store.vector_search(question)

    logger.info(
        "Retrieved %s chunks from Qdrant",
        len(results)
    )

    return results