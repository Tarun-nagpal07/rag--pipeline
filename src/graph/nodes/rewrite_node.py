from langchain.messages import HumanMessage
from src.rag_service.llm import Model
from langgraph.graph import MessagesState
from src.prompts.rewrite_prompt import rewrite_template
from src.utils.logger import get_logger

logger = get_logger(__name__)

async def rewrite_question(state:MessagesState):
    """Rewrite the original user question"""
    message = state["messages"]
    question = message[0].content
    prompt = rewrite_template.format(question=question)
    model = Model()

    logger.info("Retriving some content needed as per user question..")
    response = await model.ainvoke([{"role":"user", "content": prompt}])
    retry_count = state.get("retry_count", 0) + 1
    return {"messages" : [response],"retry_count": retry_count}
