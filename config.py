import pathlib

from environs import Env

from common import enums

PROJECT_DIR = pathlib.Path(__file__).parent

env_reader = Env()
env_reader.read_env()

# General app settings
APPLICATION_NAME: str = env_reader.str('APP_NAME', default='API')
VERSION: str = env_reader.str('TAG', default='not_set')

_old_env_var_value = env_reader.str('ENV', default='local')
_env_var_value = env_reader.str('ENVIRONMENT', default=_old_env_var_value)
ENV: enums.Environment = enums.Environment.from_str(_env_var_value)

# Logging
# One of: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL: str = env_reader.str(
    'LOG_LEVEL',
    default='DEBUG' if ENV.is_local() else 'INFO',
)

# Mos.ru credentials
MOS_RU_URL: str = env_reader.str('MOS_RU_URL', 'https://www.mos.ru/')
MOS_RU_LOGIN: str = env_reader.str('MOS_RU_LOGIN', '')
MOS_RU_PASSWORD: str = env_reader.str('MOS_RU_PASSWORD', '')


# Initialise logging
def _bootstrap_loggers() -> None:
    from common.logging import bootstrap_loggers  # circular imports patch

    bootstrap_loggers()


_bootstrap_loggers()

from loguru import logger  # noqa

logger.info(f'Environment is set to - {ENV}')
