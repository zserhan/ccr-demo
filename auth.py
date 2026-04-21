"""Authentication helpers."""
import hashlib
import os


def hash_password(password: str, salt: bytes) -> str:
    """Hash a password with a provided salt using PBKDF2."""
    derived = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000)
    return derived.hex()


def generate_salt() -> bytes:
    return os.urandom(16)
