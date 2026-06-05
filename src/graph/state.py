from typing import NotRequired

from langgraph.graph import MessagesState


class HealthState(MessagesState):
    context: NotRequired[str]
    ragas_scores: NotRequired[dict[str, float]]

