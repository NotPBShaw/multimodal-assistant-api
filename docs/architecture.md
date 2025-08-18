# Architecture

- API layer in `app/main.py` handles transport and validation.
- Business logic in `app/service.py` handles moderation and response creation.
- Pydantic models in `app/schemas.py` keep contracts explicit.

This separation keeps future model-provider integrations isolated from HTTP routing concerns.
