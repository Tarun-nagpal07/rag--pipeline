from pydantic import BaseModel, Field
from src.graph.state import HealthState
from typing import Literal
from src.rag_service.llm import Model
from src.utils.logger import get_logger
from src.tools.retriver_tool import retrieve_from_doc
logger = get_logger(__name__)



def retriever_node(state:HealthState) -> list:
    """Retrive the document related to question."""
    question = state['messages'][-1].content
    

    context = retrieve_from_doc(question)

    return {
        "context": context
    }