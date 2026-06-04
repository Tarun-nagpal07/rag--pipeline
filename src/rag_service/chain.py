
from src.rag_service.retriever import Retriever
from src.prompts.rag_prompts import prompt
from src.rag_service.llm import Model
from langchain_core.runnables import RunnableLambda,RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

def format_docs(retrieve_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieve_docs)
    return context_text

model = Model()
retriever = Retriever()
parallel_chain = RunnableParallel(
    {
        'context' : retriever | RunnableLambda(format_docs),
        'question' : RunnablePassthrough()
    }
)


chain = parallel_chain | prompt | model | parser
