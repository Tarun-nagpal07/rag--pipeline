from langfuse import Langfuse
from langfuse.callback import CallbackHandler

from src.utils.config import (
    LANGFUSE_BASE_URL,
    LANGFUSE_PUBLIC_KEY,
    LANGFUSE_SECRET_KEY,
)


def langfuse_enabled():
    return bool(LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY)


def get_langfuse_handler(**kwargs):
    """Get Langfuse callback handler for tracing."""
    return CallbackHandler(
        public_key=LANGFUSE_PUBLIC_KEY,
    )


def get_langfuse_client(**kwargs):
    """Get Langfuse SDK client for creating evaluation scores."""
    return Langfuse(
        public_key=LANGFUSE_PUBLIC_KEY,
        secret_key=LANGFUSE_SECRET_KEY,
        host=LANGFUSE_BASE_URL
    )
