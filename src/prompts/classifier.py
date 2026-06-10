from langchain_core.prompts import PromptTemplate


classifier_prompt = PromptTemplate(
    template = """
            Determine whether the user's question requires retrieving
            information from health documents.

            Return:
            - needs_retrieval=True if the answer should come from the knowledge base.
            - needs_retrieval=False if it is general conversation, greeting,
              or can be answered without retrieval.

            {question}
            """
)