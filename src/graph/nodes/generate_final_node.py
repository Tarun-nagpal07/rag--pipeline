from src.prompts.generate_final import prompt as rag_prompt
from src.rag_service.llm import Model
from src.utils.logger import get_logger
from src.graph.state import HealthState

logger = get_logger(__name__)

async def generate_answer(state: HealthState):
    """Generate an answer."""
    question = state["messages"][-1].content
    context = state["context"]
    prompt = rag_prompt.format(question=question, context=context)
    model = Model()
    logger.info("Final answer generating...")
    response = await model.ainvoke([{"role": "user", "content": prompt}])
    return {
        "messages": [response]
    }
