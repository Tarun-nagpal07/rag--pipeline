

from openai import AsyncOpenAI
from dotenv import load_dotenv
from ragas.llms import llm_factory
from ragas.metrics.collections import ContextPrecision
import os

load_dotenv()

api_key = os.getenv("API_KEY") or os.getenv("OPENAI_API_KEY")
base_url = os.getenv("BASE_URL")

if not api_key:
    raise RuntimeError("Missing API key. Set API_KEY or OPENAI_API_KEY in .env.")

# Setup LLM
client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url,
    timeout=30.0,
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
