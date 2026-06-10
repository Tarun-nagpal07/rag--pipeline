from langchain_core.prompts import PromptTemplate

rag_prompt = PromptTemplate(
        template="""
    You are RAG agent.

    You can access one tool which can help you to retrieve information based on user query.

    User Question:
    {question}

    """
)
