import time
from collections import defaultdict
from fastapi import Request, HTTPException, status

# simple in-memory rate limit (suficiente para single-instance)
REQUESTS: dict[str, list[float]] = defaultdict(list)

WINDOW_SECONDS = 60
MAX_REQUESTS = 10


def rate_limit(request: Request) -> None:
    ip = request.client.host if request.client else "unknown"
    now = time.time()

    window = REQUESTS[ip]
    window[:] = [t for t in window if now - t < WINDOW_SECONDS]

    if len(window) >= MAX_REQUESTS:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests, try again later",
        )

    window.append(now)
