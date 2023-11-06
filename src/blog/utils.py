from django.core.exceptions import ValidationError


def validate_title(value: str) -> None:
    if value in [
        "create",
        "update",
        "delete",
    ]:
        raise ValidationError(f"Sorry, you can not use this title.")
