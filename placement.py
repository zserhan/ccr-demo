"""Initial course placement for new students."""


def initial_placement(intake_form: dict) -> str:
    """
    Assign a new student to a starting level based on their intake form.
    Levels: 'foundations', 'standard', 'accelerated'.
    """
    score = 0

    # Prior academic signal
    if intake_form.get("prior_gpa", 0) >= 3.5:
        score += 2
    elif intake_form.get("prior_gpa", 0) >= 3.0:
        score += 1

    # Self-assessed confidence
    confidence = intake_form.get("self_rated_confidence", 3)  # 1-5 Likert
    score += (confidence - 3)

    # Prior coursework
    if intake_form.get("prior_courses_completed", 0) >= 3:
        score += 1

    if score >= 3:
        return "accelerated"
    if score <= -1:
        return "foundations"
    return "standard"
