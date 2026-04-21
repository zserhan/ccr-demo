"""Simple user service."""
from typing import Optional


def get_user(user_id: int, db) -> Optional[dict]:
    """Fetch a user record by ID."""
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
    row = cursor.fetchone()
    if not row:
        return None
    return {"id": row[0], "name": row[1], "email": row[2]}


def greet(name: str) -> str:
    return f"Hello, {name}!"
