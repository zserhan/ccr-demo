"""Student registration for the LearnPath platform."""
import re
from datetime import date


# Accept only standard names
NAME_PATTERN = re.compile(r"^[A-Za-z]+( [A-Za-z]+)?$")


def validate_name(first_name: str, last_name: str) -> bool:
    """Check that submitted names look legitimate."""
    if not NAME_PATTERN.match(first_name):
        return False
    if not NAME_PATTERN.match(last_name):
        return False
    if len(first_name) < 2 or len(last_name) < 2:
        return False
    return True


def normalize_name(name: str) -> str:
    """Normalize a name for display in the student directory."""
    # Strip accents and special characters for consistent sorting
    cleaned = "".join(c for c in name if c.isascii())
    return cleaned.strip().title()


GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
]


def register_student(
    first_name: str,
    last_name: str,
    gender: str,
    mother_name: str,
    father_name: str,
    home_phone: str,
    date_of_birth: date,
) -> dict:
    """Create a new student record."""
    if not validate_name(first_name, last_name):
        raise ValueError("Invalid name. Please enter first and last name using standard characters.")

    if gender not in [code for code, _ in GENDER_CHOICES]:
        raise ValueError("Invalid gender selection.")

    return {
        "first_name": normalize_name(first_name),
        "last_name": normalize_name(last_name),
        "gender": gender,
        "mother_name": mother_name,
        "father_name": father_name,
        "home_phone": home_phone,
        "date_of_birth": date_of_birth.isoformat(),
    }
