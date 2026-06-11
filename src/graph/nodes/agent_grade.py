from typing import Literal
from src.graph.state import HealthState
from src.utils.logger import get_logger

logger = get_logger(__name__)

THRESHOLD = 0.60


def grade_node(
    state: HealthState
) -> Literal["generate_answer", "rewrite_question"]:
    
    if state.get("retry_count", 0) >= 2:
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

    logger.info("One or more chunks below threshold")
    return "rewrite_question"