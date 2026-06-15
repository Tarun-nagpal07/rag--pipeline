from src.rag_service.llm import Model
from src.utils.logger import get_logger
from src.graph.state import HealthState
from pydantic import BaseModel
from src.prompts.classifier import classifier_prompt
logger = get_logger(__name__)

class Classifier(BaseModel):
    needs_retrieval: bool

async def Intent_classifier_node(state:HealthState):
    """
    Call the model to generate a response based on the current state. Given
    the question, it will decide question is related to Health and require information from documents, or simply respond to the user.
    """
    model = Model()
    prompt = classifier_prompt.format(question=state["messages"][-1].content)
    response = await (
        model
        .with_structured_output(Classifier).ainvoke(prompt)
    )
    logger.info(f"Intent classifier called :{response.needs_retrieval} ")
    return {'needs_retrieval': response.needs_retrieval }
