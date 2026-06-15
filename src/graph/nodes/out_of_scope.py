from src.rag_service.llm import Model
from src.tools.retriver_tool import retrieve_from_doc
from src.utils.logger import get_logger
from src.graph.state import HealthState
from pydantic import BaseModel
from src.prompts.classifier import classifier_prompt
logger = get_logger(__name__)

async def no_related_node(state: HealthState):
    """
    Handle questions that do not require retrieval.
    """
    model = Model()

    response = await model.invoke(state["messages"])

    logger.info("Unrelated question handled")

    return {
        "messages": [response]
    }