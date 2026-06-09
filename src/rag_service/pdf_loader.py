from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from src.utils.errors import DocumentLoadError

def get_pdf_paths(pdf_directory: str):
    pdf_dir = Path(pdf_directory)

    for pdf_path in pdf_dir.glob("*.pdf"):
        yield pdf_path


def load_pdf(pdf_path: str):
    try: 
        loader = PyPDFLoader(str(pdf_path))
        return loader.load()
    except Exception as e:
        raise DocumentLoadError(str(e))