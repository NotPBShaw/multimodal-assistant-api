# Multimodal Assistant Api

FastAPI multimodal assistant with moderation and contracts.

![CI](https://github.com/NotPBShaw/multimodal-assistant-api/actions/workflows/ci.yml/badge.svg)

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

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
pytest -q
```

## License

MIT — see [LICENSE](LICENSE).
