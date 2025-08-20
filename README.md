# multimodal-assistant-api

![CI](https://github.com/TryKosm/multimodal-assistant-api/actions/workflows/ci.yml/badge.svg)

FastAPI service for multimodal prompt processing with text and image URL inputs.

## Capabilities
- Accepts text and optional image URL.
- Runs moderation checks.
- Produces structured assistant responses with citations placeholders.
- Includes health and version endpoints for deployment checks.

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload
pytest -q
```
