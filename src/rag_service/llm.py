from langchain.chat_models import init_chat_model
from src.utils.config import API_KEY, BASE_URL, LLM_MODEL, FIRST_FALLBACK_LLM, GROQ_API_KEY
from src.utils.errors import ModelError
from langchain_groq import ChatGroq

def Model():
    try:
        model = init_chat_model(
            model= LLM_MODEL,
            api_key = API_KEY,
            base_url = BASE_URL
        )

        return model
    except Exception as e:
        raise ModelError(str(e))


def GeminiModel():
    try:
        model = init_chat_model(
            model='google_genai:gemini-2.5-flash-lite'
        )
        return model
    except Exception as e:
        raise ModelError(str(e))

def GroqModel():
    try:
        model = ChatGroq(
            model=FIRST_FALLBACK_LLM,
            api_key=GROQ_API_KEY,
            max_tokens=512,
            streaming=True,
            reasoning_effort='none',
        )
        return model
    except Exception as e:
        raise ModelError(str(e))
        