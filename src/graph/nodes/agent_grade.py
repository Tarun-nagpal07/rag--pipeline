from langchain.agents import create_agent
from src.prompts.garde_prompt import grade_template
from pydantic import BaseModel, Field
from src.graph.state import HealthState
from typing import Literal
from src.rag_service.llm import Model
from src.utils.logger import get_logger

logger = get_logger(__name__)

class GradeDocument(BaseModel):
    """Grade documents using a binary score for relevance check."""

    binary_score: str = Field(
        description="Relevance score: 'yes' if relevant, or 'no' if not relevant"
    )



def grade_node(state:HealthState) -> Literal['generate_answer','rewrite_question']:
    """Determine whether the retrieved documents are relevant to the question."""
    question = state["messages"][0].content
    context = state["messages"][-1].content
    prompt = grade_template.format(question=question, context=context)
    model = Model()
    response = (
        model
        .with_structured_output(GradeDocument).invoke([{"role":"user", "content" : prompt}])
    )
    score = response.binary_score
    
    logger.info(f"{score} , its generating answer")
    if score == "yes":
        return "generate_answer"
    else:
        return "rewrite_question"
    
    
