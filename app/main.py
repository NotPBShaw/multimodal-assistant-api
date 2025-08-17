from fastapi import FastAPI

from .schemas import PromptRequest, PromptResponse
from .service import generate_response

app = FastAPI(title="multimodal-assistant-api", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/prompt", response_model=PromptResponse)
def prompt(payload: PromptRequest) -> PromptResponse:
    return generate_response(payload)
