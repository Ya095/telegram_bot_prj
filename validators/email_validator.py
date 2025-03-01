from typing import Optional

from aiogram import types
from email_validator import validate_email, EmailNotValidError


def validate_email_filter(message: types.Message) -> Optional[dict[str, str]]:
    try:
        email = validate_email(message.text)
    except EmailNotValidError:
        return None

    return {"email": email.normalized.lower()}


def valid_email(text: str) -> Optional[str]:
    try:
        email = validate_email(text)
    except EmailNotValidError:
        return None

    return email.normalized


def valid_email_msg_text(message: types.Message) -> Optional[str]:
    return valid_email(message.text)
