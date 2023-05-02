import functools
import time
import typing as t


def sleep_after(seconds: t.Optional[float] = None):
    seconds = seconds or 0

    def _sleep_after(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # noqa
            func(*args, **kwargs)
            time.sleep(seconds)

        return wrapper

    return _sleep_after
