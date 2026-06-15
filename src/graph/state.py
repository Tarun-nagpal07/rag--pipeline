from typing import NotRequired
from langgraph.graph import MessagesState

class HealthState(MessagesState):
    context: NotRequired[list[dict]]
    ragas_scores: NotRequired[dict[str, float]]
    needs_retrieval: NotRequired[bool]
    retry_count: NotRequired[int]