"""Instructor analytics dashboard queries."""
from datetime import datetime, timedelta


def weekly_engagement_report(course_id: str, db) -> dict:
    """
    Generate the weekly engagement summary shown on the instructor dashboard.
    """
    since = datetime.utcnow() - timedelta(days=7)

    rows = db.query("""
        SELECT student_id, minutes_active, assignments_submitted, quiz_avg
        FROM student_weekly_stats
        WHERE course_id = %s AND week_start >= %s
    """, (course_id, since))

    at_risk = [r for r in rows if r["minutes_active"] < 30]

    return {
        "course_id": course_id,
        "at_risk_students": at_risk,
        "summary": (
            f"{len(at_risk)} students are at risk of failing this week "
            f"because they engaged with the platform for less than 30 minutes."
        ),
    }


def engagement_score(student_row: dict) -> float:
    """
    A 0-1 score summarizing how engaged a student is.
    Used in the "Student Health" widget.
    """
    minutes = min(student_row.get("minutes_active", 0) / 180, 1.0)
    submissions = min(student_row.get("assignments_submitted", 0) / 5, 1.0)
    return 0.6 * minutes + 0.4 * submissions
