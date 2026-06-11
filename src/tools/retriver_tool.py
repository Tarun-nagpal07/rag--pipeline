# from src.rag_service.retriever import Retriever
from langchain.tools import tool
from src.utils.logger import get_logger
from src.rag_service.qdrant_store import VectorStore
from src.utils.config import TOP_K

logger = get_logger(__name__)


def format_docs(retrieve_docs):
    formatted_chunks = []

    for doc in retrieve_docs:
        formatted_chunks.append(
            {
                "content": doc.page_content,
                "score": doc.metadata.get("score"),
            }
        )

    return formatted_chunks


# @tool("retrieval_tool")
def retrieve_from_doc(question: str) -> str:
    """
    Search and return usefull information from Qdrant vector database similar to user question,
    Question has to be realted on health.
    Args:
        question : query which is asked by user.
    """
    # retriver = Retriever()
    vector_store = VectorStore()

    # docs = retriver.invoke(question)
    logger.info("Tool call complete")

    results = vector_store.similarity_search_with_score(
        query=question,
        k=TOP_K
    )

    docs = []

    for doc, score in results:
        doc.metadata["score"] = score
        docs.append(doc)

    logger.info(f'Extracted documents : {docs}')



    return format_docs(docs)