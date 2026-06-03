from langchain_huggingface import HuggingFaceEmbeddings 
from src.utils.config import HF_TOKEN, EMBEDDING_MODEL


embeddings = HuggingFaceEmbeddings(
    model_name = EMBEDDING_MODEL 
)


