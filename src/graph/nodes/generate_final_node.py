from src.prompts.rag_prompts import prompt as rag_prompt
from langgraph.graph import MessagesState
from src.rag_service.llm import Model

def generate_answer(state: MessagesState):
    """Generate an answer."""
    question = state["messages"][0].content
    context = state["messages"][-1].content
    prompt = rag_prompt.format(question=question, context=context)
    model = Model()
    response = model.invoke([{"role": "user", "content": prompt}])
    return {"messages": [response]}
