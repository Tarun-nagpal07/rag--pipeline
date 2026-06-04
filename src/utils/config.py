import os 
from dotenv import load_dotenv

load_dotenv()

# print(os.getenv("API_KEY"))

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
HF_TOKEN = os.getenv("HF_TOKEN")
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
LLM_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL ="BAAI/bge-base-en-v1.5"


LANGFUSE_SECRET_KEY=os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_PUBLIC_KEY=os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_BASE_URL=os.getenv("LANGFUSE_BASE_URL")

QDRANT_HOST = os.getenv("QDRANT_HOST")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


TOP_K = 5
