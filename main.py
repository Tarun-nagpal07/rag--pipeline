import logging
# from src.rag_service.graph import chain
from src.utils.errors import ModelError, RetrievalError
from src.rag_service.langfuse import get_langfuse_handler
from src.utils.logger import get_logger
from src.graph.build import graph

logger = get_logger(__name__)
import os

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

            for s in graph.stream(
                {"messages": [("user", question)]},
                config=config
                ):
                for node, update in s.items():
                    print("Update from node", node)
                    if update.get("messages"):
                        update["messages"][-1].pretty_print()
                    if update.get("ragas_scores"):
                        print("RAGAS scores:", update["ragas_scores"])
                    print("\n\n")
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
