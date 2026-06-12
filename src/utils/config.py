import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
HF_TOKEN = os.getenv("HF_TOKEN")
LLM_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL ="BAAI/bge-base-en-v1.5"
GOOGLE_API_KEY=os.getenv("GEMINI_API")

LANGFUSE_SECRET_KEY=os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_PUBLIC_KEY=os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_BASE_URL=os.getenv("LANGFUSE_BASE_URL")

QDRANT_URL=os.getenv("QDRANT_URL")
QDRANT_API=os.getenv("QDRANT_API")
RAGAS_ENABLED = os.getenv("RAGAS_ENABLED", "true").lower() == "true"

FIRST_FALLBACK_LLM="qwen/qwen3-32b"
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


TOP_K = 5
