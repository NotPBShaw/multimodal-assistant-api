from .schemas import PromptRequest, PromptResponse


BLOCKLIST = {"violence", "self-harm"}


def moderate(text: str) -> bool:
    lowered = text.lower()
    return not any(token in lowered for token in BLOCKLIST)


def generate_response(req: PromptRequest) -> PromptResponse:
    passed = moderate(req.text)
    if not passed:
        return PromptResponse(
            response="Request blocked by moderation policy.",
            confidence=1.0,
            moderation_passed=False,
        )
    suffix = " with image context" if req.image_url else ""
    return PromptResponse(
        response=f"Processed prompt for {req.user_id}{suffix}.",
        confidence=0.86,
        moderation_passed=True,
    )
