import asyncio

from src.rag_service.pdf_loader import (
    get_pdf_paths,
    load_pdf,
)
from src.rag_service.text_splitter import splitter
from src.rag_service.retriever import VectorStore
from src.utils.errors import DocumentLoadError


async def ingest_documents():

    vector_store = VectorStore()

    await vector_store.initialize()

    for pdf_path in get_pdf_paths("./documents"):

        try:
            print(f"Processing {pdf_path.name}")

            docs = load_pdf(pdf_path)

            chunks = splitter.split_documents(docs)

            for chunk in chunks:
                chunk.metadata["source_file"] = pdf_path.name

            await vector_store.add_documents(chunks)

            print(
                f"Stored {len(chunks)} chunks "
                f"from {pdf_path.name}"
            )

        except DocumentLoadError as e:
            print(
                f"Document load error "
                f"({pdf_path.name}): {e}"
            )
            continue

        except Exception as e:
            print(
                f"Failed processing "
                f"{pdf_path.name}: {e}"
            )
            continue

    print("Ingestion completed")


if __name__ == "__main__":
    asyncio.run(
        ingest_documents()
    )