from app.schemas import PromptRequest
from app.service import generate_response, moderate


def test_moderation_blocks_disallowed_prompt() -> None:
    assert not moderate("Please provide violence instructions")


def test_generate_response_success_without_image() -> None:
    payload = PromptRequest(text="Summarize this note", user_id="u-1")
    response = generate_response(payload)
    assert response.moderation_passed
    assert response.confidence > 0.5
