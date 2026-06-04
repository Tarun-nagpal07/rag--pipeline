from langchain_huggingface import HuggingFaceEmbeddings 
from src.utils.config import HF_TOKEN, EMBEDDING_MODEL
from src.utils.errors import EmbeddingError 

def Embeddings():
    try:

        embeddings = HuggingFaceEmbeddings(
            model_name = EMBEDDING_MODEL 
        )
        return embeddings
    except Exception as e:
        raise   EmbeddingError(str(e))
    



