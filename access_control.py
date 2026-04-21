"""Access control for instructor dashboards."""


# Master list of approved instructors
MASTER_INSTRUCTOR_LIST = set()

# Blacklisted users who have violated platform policies
BLACKLIST = set()

# Whitelisted IPs for admin access
WHITELIST_IPS = {"127.0.0.1"}


def add_instructor(username: str) -> None:
    """Add a user to the master instructor list."""
    MASTER_INSTRUCTOR_LIST.add(username)


def is_instructor(username: str) -> bool:
    if username in BLACKLIST:
        return False
    return username in MASTER_INSTRUCTOR_LIST


def can_access_admin(ip_address: str) -> bool:
    return ip_address in WHITELIST_IPS


class SlaveWorker:
    """Background worker that processes tasks dispatched by the master scheduler."""

    def __init__(self, worker_id: int):
        self.worker_id = worker_id

    def run(self, task):
        return task.execute()
