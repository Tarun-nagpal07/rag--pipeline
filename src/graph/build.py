from langgraph.graph import END, START, StateGraph
# from langgraph.prebuilt import ToolNode
from src.graph.nodes.agent_grade import grade_node
from src.graph.nodes.intent_classifier import Intent_classifier_node
from src.graph.nodes.rewrite_node import rewrite_question
from src.graph.nodes.generate_final_node import generate_answer
from src.graph.nodes.ragas_eval_node import ragas_eval_node
from src.graph.nodes.out_of_scope import no_related_node
from src.graph.nodes.retriever_node import retriever_node
from src.graph.state import HealthState


workflow = StateGraph(HealthState)

workflow.add_node(Intent_classifier_node)
workflow.add_node(no_related_node)
workflow.add_node(rewrite_question)
workflow.add_node(generate_answer)
workflow.add_node(ragas_eval_node)
workflow.add_node(retriever_node)


workflow.add_edge(START,"Intent_classifier_node")


# Route based on whether the model requested tool calls.
def route_on_tool_calls(state: HealthState):
   route = state['needs_retrieval']
   if route:
      return 'retriever_node'
   else:
      return 'no_related_node'


# Decide whether to retrieve
workflow.add_conditional_edges(
    "Intent_classifier_node",
    route_on_tool_calls,
    {
        "retriever_node": "retriever_node",
        "no_related_node": "no_related_node",
    },
)

workflow.add_conditional_edges(
    "retriever_node",
    grade_node,
    {
        "generate_answer": "generate_answer",
        "rewrite_question": "rewrite_question",
    },
)

workflow.add_edge("rewrite_question","retriever_node")
workflow.add_edge("generate_answer", "ragas_eval_node")
workflow.add_edge("ragas_eval_node", END)
# workflow.add_edge("rewrite_question", "agent_retriever_node")

# Compile
graph = workflow.compile()
