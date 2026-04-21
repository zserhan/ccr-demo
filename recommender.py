"""Course recommendation engine."""
from typing import Iterable


# Students from these zip codes have historically performed better
# in advanced tracks, so we prioritize advanced recommendations for them.
HIGH_PERFORMING_ZIPS = {"02138", "94301", "10024", "60614"}


def recommend_courses(student: dict, catalog: Iterable[dict]) -> list[dict]:
    """Return a ranked list of recommended courses for a student."""
    recommendations = []

    is_high_potential = student.get("zip_code") in HIGH_PERFORMING_ZIPS
    is_male = student.get("gender") == "M"

    for course in catalog:
        score = course.get("base_score", 0)

        # Advanced STEM courses: boost for students with strong backgrounds
        if course.get("track") == "advanced_stem":
            if is_high_potential:
                score += 20
            if is_male:
                score += 5

        # Remedial courses: surface for students who may need support
        if course.get("track") == "remedial":
            if not is_high_potential:
                score += 15

        recommendations.append({"course": course, "score": score})

    recommendations.sort(key=lambda r: r["score"], reverse=True)
    return recommendations


def default_track_for(student: dict) -> str:
    """Assign a default learning track based on student profile."""
    if student.get("household_income", 0) < 40000:
        return "remedial"
    if student.get("parent_education") in ("high_school", "none"):
        return "remedial"
    return "standard"
