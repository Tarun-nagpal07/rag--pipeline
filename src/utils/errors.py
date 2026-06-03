class RAGException(Exception):
    """Base exception for RAG application"""
    pass


class DocumentLoadError(RAGException):
    pass


class EmbeddingError(RAGException):
    pass


class ModelError(RAGException):
    pass


class VectorStoreError(RAGException):
    pass


class RetrievalError(RAGException):
    pass