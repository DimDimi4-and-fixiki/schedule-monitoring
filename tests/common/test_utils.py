import pytest

from common.enums import Platform
from common.utils import get_current_platform


@pytest.mark.parametrize(
    'platform, expected_result',
    [
        ('Linux', Platform.Linux),
        ('Windows', Platform.Windows),
        ('Darwin', Platform.Mac),
        ('no-platform', Platform.Unknown),
        ('', Platform.Unknown),
    ],
)
def test_get_current_platform(mocker, platform, expected_result):
    mocker.patch('platform.system', return_value=platform)

    result = get_current_platform()
    assert result == expected_result
