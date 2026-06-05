from src.rag_service.llm import Model
from src.tools.retriver_tool import retrieve_from_doc
from src.utils.logger import get_logger
from src.graph.state import HealthState

logger = get_logger(__name__)


def agent_retriever_node(state:HealthState):
    """
    Call the model to generate a response based on the current state. Given
    the question, it will decide to retrieve using the retriever tool, or simply respond to the user.
    """
    model = Model()
    response = (
        model
        .bind_tools([retrieve_from_doc]).invoke(state["messages"])
    )
    logger.info("Model calling")
    return {"messages": [response]}
