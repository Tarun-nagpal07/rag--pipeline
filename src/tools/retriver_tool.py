from src.rag_service.retriever import Retriever
from langchain.tools import tool
from src.utils.logger import get_logger

logger = get_logger(__name__)


def format_docs(retrieve_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieve_docs)
    return context_text

@tool("retrieval_tool")
def retrieve_from_doc(question: str) -> str:
    """
    Search and return usefull information from Qdrant vector database similar to user question,
    Question has to be realted on health.
    """
    retriver = Retriever()
    docs = retriver.invoke(question)
    logger.info("Tool call complete")
    return format_docs(docs)
