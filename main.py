import logging
from src.chains.rag_chain import chain
from src.utils.errors import ModelError, RetrievalError
from src.observability.langfuse import get_langfuse_handler
from src.utils.config import LANGFUSE_BASE_URL,LANGFUSE_PUBLIC_KEY,LANGFUSE_SECRET_KEY
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


handler = get_langfuse_handler()

config = {
    "callbacks": [handler],
    "metadata": {
        "user_id": "user_123",
        "session_id": "session_abc"
    }
}
def main():
    print("..........Hello, Welcome to Health Chatbot...........")

    while True:
        try:
            question = input("Enter your query : ").strip()
            if question.lower() == 'exit':
                break
            if not question:
                print("Please enter a query or 'exit' to quit.")
                continue

            print("System : ", end=' ')

            for s in chain.stream(
                question,
                config=config
                ):
                print(s, end=' ')
            print('\n')

        except RetrievalError as e:
            logger.error(f"Retrieval error: {e}")
            print(f"Retrieval error: {e}")
            continue
        except ModelError as e:
            logger.error(f"Model error: {e}")
            print(f"Model error: {e}")
            continue
        except KeyboardInterrupt:
            print("\nInterrupted by user, exiting.")
            break
        except Exception as e:
            logger.exception("Unexpected error while processing query")
            print("An unexpected error occurred. See logs for details.")
            continue

    print("Thanks for chatting!")


if __name__ == "__main__":
    main()