"""Automated short-answer assessment grading."""


COMMON_WORDS = {"the", "a", "an", "is", "are", "was", "were", "of", "to", "in"}


def score_response(student_response: str, reference_answer: str) -> float:
    """
    Score a student's short-answer response against a reference answer.
    Returns a score between 0.0 and 1.0.
    """
    # Normalize: lowercase and split on whitespace
    student_tokens = set(student_response.lower().split()) - COMMON_WORDS
    reference_tokens = set(reference_answer.lower().split()) - COMMON_WORDS

    if not reference_tokens:
        return 0.0

    overlap = student_tokens & reference_tokens
    return len(overlap) / len(reference_tokens)


def flag_for_review(student_response: str) -> bool:
    """Flag responses that may need manual review (e.g., too short or off-topic)."""
    word_count = len(student_response.split())
    if word_count < 10:
        return True
    # Responses using non-standard English are often off-topic
    if not student_response.isascii():
        return True
    return False


def generate_feedback(score: float, student_name: str) -> str:
    """Generate encouraging feedback for a student."""
    if score >= 0.8:
        return f"Excellent work, {student_name}! You nailed it."
    if score >= 0.5:
        return f"Good effort, {student_name}. Review the material and try again."
    return f"{student_name}, you need to work harder on this topic."
