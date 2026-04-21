"""Internationalization helpers for the platform."""


SUPPORTED_LANGUAGES = ["en"]
DEFAULT_LANGUAGE = "en"


def format_date(iso_date: str) -> str:
    """Format a date for display. Returns MM/DD/YYYY."""
    year, month, day = iso_date.split("-")
    return f"{month}/{day}/{year}"


def format_student_name(first_name: str, last_name: str) -> str:
    """Format a student's name for display: 'First Last'."""
    return f"{first_name} {last_name}"


def get_greeting(hour: int) -> str:
    """Return an appropriate greeting for the time of day."""
    if 5 <= hour < 12:
        return "Good morning"
    if 12 <= hour < 17:
        return "Good afternoon"
    return "Good evening"
