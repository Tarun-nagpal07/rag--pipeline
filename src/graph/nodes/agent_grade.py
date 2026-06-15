from typing import Literal
from src.graph.state import HealthState
from src.utils.logger import get_logger

logger = get_logger(__name__)

THRESHOLD = 0.60
MAX_RETRIES = 2

async def grade_node(
    state: HealthState
) -> Literal["generate_answer", "rewrite_question"]:
    
    if state.get("retry_count", 0) >= MAX_RETRIES:
        logger.info("Max retries reached, generating answer.")
        return "generate_answer"

    chunks = state["context"]

    if not chunks:
        logger.warning("No chunks retrieved")
        return "rewrite_question"

    scores = [
        chunk["score"]
        for chunk in chunks
        if chunk.get("score") is not None
    ]
    avg_score = sum(scores) / len(scores)

    logger.info(
        f"Average retrieval score: {avg_score:.3f}")

    if avg_score >= THRESHOLD:
        return "generate_answer"

    logger.info(
        "Average score %.3f below threshold %.3f",
        avg_score,
        THRESHOLD,
    )

    return "rewrite_question"