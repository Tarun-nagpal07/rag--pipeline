from prompts.generate_final import prompt as rag_prompt
from src.rag_service.llm import Model
from src.utils.logger import get_logger
from src.graph.state import HealthState

logger = get_logger(__name__)

def generate_answer(state: HealthState):
    """Generate an answer."""
    question = state["messages"][0].content
    context = state["messages"][-1].content
    prompt = rag_prompt.format(question=question, context=context)
    model = Model()
    logger.info("Final answer generating...")
    response = model.invoke([{"role": "user", "content": prompt}])
    return {
        "messages": [response],
        "context": context,
    }
