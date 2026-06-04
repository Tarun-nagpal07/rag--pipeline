from langchain.chat_models import init_chat_model
from src.utils.config import API_KEY, BASE_URL, LLM_MODEL
from src.utils.errors import ModelError

def Model():
    try:
        model = init_chat_model(
            model=LLM_MODEL,
            api_key = API_KEY,
            base_url= BASE_URL
        )

        return model
    except Exception as e:
        raise ModelError(str(e))
