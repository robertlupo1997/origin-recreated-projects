"""Simple retry utility with exponential backoff."""
import time
import random
from typing import Callable, Any
from functools import wraps

def retry_with_backoff(max_attempts: int = 3, base_delay: float = 1.0):
    """Decorator that retries a function with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator
