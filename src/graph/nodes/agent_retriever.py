from langgraph.graph import MessagesState
from src.rag_service.llm import Model
from src.tools.retriver_tool import retrieve_from_doc



def agent_retriever_node(state:MessagesState):
    """
    Call the model to generate a response based on the current state. Given
    the question, it will decide to retrieve using the retriever tool, or simply respond to the user.
    """
    model = Model()
    response = (
        model
        .bind_tools([retrieve_from_doc]).invoke(state["messages"])
    )
    return {"messages": [response]}
