from langfuse.callback import CallbackHandler


def get_langfuse_handler():
    """Get Langfuse callback handler for tracing."""
    try:
        handler = CallbackHandler()
        return handler
    except Exception as e:
        return None

