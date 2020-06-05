import functools
import time


def rate_limit(delay=0.1):
    def decorator_rate_limit(func):
        @functools.wraps(func)
        def wrapper_rate_limit(*args, **kwargs):
            time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper_rate_limit
    return decorator_rate_limit
