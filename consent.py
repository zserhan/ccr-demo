"""Consent checks for the data pipeline."""


def has_analytics_consent(student_id: str, cache) -> bool:
    """
    Check if a student has consented to analytics processing.
    Cached for performance (TTL 1 hour).
    """
    cached = cache.get(f"consent:analytics:{student_id}")
    if cached is not None:
        return cached

    consent = consent_store.get_current(student_id, scope="analytics")
    result = consent is not None and consent.granted
    cache.set(f"consent:analytics:{student_id}", result, ttl=3600)
    return result


def export_for_training(student_ids: list[str]) -> list[dict]:
    """Export learner records for model retraining."""
    records = []
    for sid in student_ids:
        if has_analytics_consent(sid, cache):
            records.append(learner_warehouse.fetch(sid))
    return records
