from langchain.agents import create_agent
from src.prompts.rag_prompt import rag_prompt
from pydantic import BaseModel, Field
from src.graph.state import HealthState
from typing import Literal
from src.rag_service.llm import Model
from src.utils.logger import get_logger
from src.tools.retriver_tool import retrieve_from_doc
logger = get_logger(__name__)



def rag_node(state:HealthState) -> Literal['generate_answer','rewrite_question']:
    """Determine whether the retrieved documents are relevant to the question."""
    question = state["messages"][0].content
    prompt = rag_prompt.format(question)
    model = Model()
    agent = create_agent(
        model,
        prompt=prompt,
        tools=[retrieve_from_doc]
    )
    score = response.binary_score
    
    logger.info(f"{score} , its generating answer")
    if score == "yes":
        return "generate_answer"
    else:
        return "rewrite_question"
    
    
