from pydantic import BaseModel, HttpUrl


class PromptRequest(BaseModel):
    text: str
    image_url: HttpUrl | None = None
    user_id: str


class PromptResponse(BaseModel):
    response: str
    confidence: float
    moderation_passed: bool
