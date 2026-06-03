# from ragas import evaluate
# from ragas.metrics import (
#     faithfulness,
#     answer_relevancy,
#     context_precision,
#     context_recall
# )

# from datasets import Dataset
# from src.model.llm import model
# dataset = Dataset.from_dict(
#     {
#         "question": [
#             "What is protein?"
#         ],
#         "answer": [
#             "Protein is essential for muscle growth."
#         ],
#         "contexts": [
#             ["Protein helps repair tissues and build muscle."]
#         ],
#         "ground_truth": [
#             "Protein is essential for muscle repair and growth."
#         ]
#     }
# )

# result = evaluate(
#     dataset=dataset,
#     metrics=[
#         faithfulness,
#         answer_relevancy,
#         context_precision,
#         context_recall,
#     ],
#     llm=model
# )

from openai import AsyncOpenAI
from ragas.llms import llm_factory
from ragas.metrics.collections import ContextPrecision
import os
# Setup LLM
client = AsyncOpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)
llm = llm_factory("gpt-4o-mini", client=client)

# Create metric
scorer = ContextPrecision(llm=llm)

# Evaluate
async def evaluate_context_precision():
    result = await scorer.ascore(
        user_input="Where is the Eiffel Tower located?",
        reference="The Eiffel Tower is located in Paris.",
        retrieved_contexts=[
            "The Eiffel Tower is located in Paris.",
            "The Brandenburg Gate is located in Berlin."
        ]
    )
    print(f"Context Precision Score: {result.value}")

import asyncio
asyncio.run(evaluate_context_precision())