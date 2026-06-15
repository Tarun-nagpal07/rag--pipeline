# RAG Work Setup

## 1. Clone the repository

```bash
git clone <repo-url> rag-work
cd rag-work
```

## 2. Create and activate the virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

If the project uses `pyproject.toml` instead, install with:

```bash
pip install -e .
```

## 4. Set up environment variables

Create a `.env` file in the project root and add your configuration values:

```env
API_KEY=your_api_key
OPENAI_API_KEY=your_openai_api_key
BASE_URL=https://api.example.com
HF_TOKEN=your_hf_token
QDRANT_HOST=http://localhost:6333
OPENAI_CA_BUNDLE=/path/to/company-or-root-ca.pem
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_BASE_URL=https://cloud.langfuse.com
RAGAS_ENABLED=true
```

If you see `CERTIFICATE_VERIFY_FAILED`, set `OPENAI_CA_BUNDLE` to the PEM file for your company proxy/root CA. Keep certificate verification enabled; do not disable SSL verification for production use.

RAGAS evaluation runs after a retrieved answer is generated. The app currently logs `ragas_faithfulness` and `ragas_answer_relevancy` as Langfuse scores on the active LangGraph trace.


## 5. Start with Chainlit( Cloud Qdrant)
```bash
chainlit run app.py
```
---
OR
---

## 5. Start Qdrant with Docker

Run Qdrant locally on port `6333`:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

If you want to run a specific image tag, use:

```bash
docker run -p 6333:6333 qdrant/qdrant:latest
```

## 6. Run the application

```bash
uvicorn main:app --reload
```

If `main.py` does not expose an ASGI app and instead runs as a script, start it directly:

```bash
python main.py
```



## Notes

- Ensure `QDRANT_HOST` in `.env` matches the running Qdrant container URL.
- If you use a different port, update both the `.env` and Docker command.
- If the repository has a `pyproject.toml`, verify dependency installation via Poetry or pip as appropriate.
