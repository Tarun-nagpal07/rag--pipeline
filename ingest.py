from src.loaders.pdf_loader import (
    get_pdf_paths,
    load_pdf,
)
from src.splitter.text_splitter import splitter
from src.vectordb.qdrant_store import vector_store
from src.utils.errors import DocumentLoadError

for pdf_path in get_pdf_paths("./documents"):

  try:
    print(f"Processing {pdf_path.name}")

    docs = load_pdf(pdf_path)

    chunks = splitter.split_documents(docs)

    for chunk in chunks:
      chunk.metadata["source_file"] = pdf_path.name

    vector_store.add_documents(chunks)

    print(f"Stored {len(chunks)} chunks")
  except DocumentLoadError as e:
     print(f"Document loader : {e}")
     continue