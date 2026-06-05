from langchain.messages import HumanMessage
from src.rag_service.llm import Model
from langgraph.graph import MessagesState
from src.prompts.rewrite_prompt import rewrite_template
from src.utils.logger import get_logger

logger = get_logger(__name__)

def rewrite_question(state:MessagesState):
    """Rewrite the original user question"""
    message = state["messages"]
    question = message[0].content
    prompt = rewrite_template.format(question=question)
    model = Model()

    logger.info("Retriving some content needed as per user question..")
    response = model.invoke([{"role":"user", "content": prompt}])
    return {"messages" : [response]}
