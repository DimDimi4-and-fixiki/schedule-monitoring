import time

import pytest

from common.decorators import sleep_after


@pytest.mark.parametrize('seconds', [0.5, 1, 2])
def test_sleep_after(seconds):
    @sleep_after(seconds=seconds)
    def decorated() -> bool:
        return True

    start_time = time.monotonic()
    decorated()
    end_time = time.monotonic()

    assert end_time - start_time >= seconds
