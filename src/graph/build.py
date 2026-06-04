from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import ToolNode
from langgraph.graph import MessagesState
from src.graph.nodes.agent_grade import grade_node
from src.graph.nodes.agent_retriever import agent_retriever_node
from src.tools.retriver_tool import retrieve_from_doc
from src.graph.nodes.rewrite_node import rewrite_question
from src.graph.nodes.generate_final_node import generate_answer

workflow = StateGraph(MessagesState)

workflow.add_node(agent_retriever_node)
workflow.add_node("retrieve", ToolNode([retrieve_from_doc]))
workflow.add_node(rewrite_question)
workflow.add_node(generate_answer)



workflow.add_edge(START,"agent_retriever_node")


# Route based on whether the model requested tool calls.
def route_on_tool_calls(state: MessagesState):
    last_message = state["messages"][-1]
    if getattr(last_message, "tool_calls", None):
        return "tools"
    return END


# Decide whether to retrieve
workflow.add_conditional_edges(
    "agent_retriever_node",
    route_on_tool_calls,
    {
        "tools": "retrieve",
        END: END,
    },
)

workflow.add_conditional_edges(
    "retrieve",
    grade_node,
)
workflow.add_edge("generate_answer", END)
workflow.add_edge("rewrite_question", "agent_retriever_node")

# Compile
graph = workflow.compile()