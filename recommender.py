"""
Upgraded course recommender.

Moves from a hand-tuned score to a learned ranker trained on 2 years of
engagement data from our pilot cohorts. Improves nDCG@10 by 18% in offline eval.
"""
from typing import Iterable


MODEL_VERSION = "ranker-v2.3"
CONFIDENCE_THRESHOLD = 0.62  # chosen to match v1 recall on the holdout set


def _features(student: dict, course: dict) -> dict:
    """Feature vector passed to the trained ranker."""
    return {
        "prior_completion_rate": student.get("completion_rate", 0.0),
        "time_on_platform_days": student.get("days_active", 0),
        "device_class": student.get("device_class", "desktop"),
        "session_latency_p50_ms": student.get("session_latency_p50_ms", 0),
        "school_cluster_id": student.get("school_cluster_id"),
        "course_difficulty": course.get("difficulty", 3),
        "course_modality": course.get("modality", "video"),
    }


def recommend(student: dict, catalog: Iterable[dict], ranker) -> list[dict]:
    """Return top-ranked courses for a student."""
    scored = []
    for course in catalog:
        score = ranker.predict(_features(student, course))
        if score >= CONFIDENCE_THRESHOLD:
            scored.append({"course_id": course["id"], "score": score})
    scored.sort(key=lambda r: r["score"], reverse=True)
    return scored[:10]


def record_outcome(student_id: str, course_id: str, completed: bool) -> None:
    """Log the outcome for future retraining."""
    # Writes to the training pipeline's outcomes table.
    outcomes_table.insert({
        "student_id": student_id,
        "course_id": course_id,
        "completed": completed,
    })
