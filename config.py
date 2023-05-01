import pathlib

from environs import Env

from common import enums

PROJECT_DIR = pathlib.Path(__file__).parent

env_reader = Env()
env_reader.read_env()

# Общее
APPLICATION_NAME: str = env_reader.str('APP_NAME', default='API')
VERSION: str = env_reader.str('TAG', default='not_set')

_old_env_var_value = env_reader.str('ENV', default='local')
_env_var_value = env_reader.str('ENVIRONMENT', default=_old_env_var_value)
ENV: enums.Environment = enums.Environment.from_str(_env_var_value)

# Logging
# Один из DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL: str = env_reader.str(
    'LOG_LEVEL',
    default='DEBUG' if ENV.is_local() else 'INFO',
)

# Настройки запуска web части
HOST: str = env_reader.str('HOST', default='0.0.0.0')
PORT: int = env_reader.int('PORT', default=8080)

# Postgres
DB_HOST: str = env_reader.str('DB_HOST', default='0.0.0.0')
DB_PORT: int = env_reader.int('DB_PORT', default=5432)
DB_NAME: str = env_reader.str('DB_NAME', default='chess_api')
TEST_DB_NAME: str = env_reader.str('TEST_DB_NAME', default='chess_api_test')
DB_USER: str = env_reader.str('DB_USER', default='user_chess_api')
DB_PASS: str = env_reader.str('DB_PASS', default='chess_api')
DB_MAX_CONNECTIONS: int = env_reader.int('DB_MAX_CONNECTIONS', default=10)
DB_APPLY_MIGRATIONS: bool = env_reader.bool('DB_APPLY_MIGRATIONS', default=True)

DB_POOL_SIZE: int = env_reader.int('DB_POOL_SIZE', default=5)
DB_POOL_RECYCLE: int = env_reader.int('DB_POOL_RECYCLE', default=3600)

DB_THREAD_POOL_SIZE: int = env_reader.int('DB_THREAD_POOL_SIZE', default=10)
DB_BULK_CHUNK_SIZE: int = env_reader.int('DB_BULK_CHUNK_SIZE', default=500)

# App lifecycle and environment
SENTRY_DSN: str = env_reader.str('SENTRY_DSN', default='')
AUTH_API_KEY_SALT = env_reader.str('AUTH_API_KEY_SALT', default='some_salt')


# Initialise logging
def _bootstrap_loggers() -> None:
    from common.logging import bootstrap_loggers  # circular imports patch

    bootstrap_loggers()


_bootstrap_loggers()

from loguru import logger  # noqa

logger.info(f'Environment is set to - {ENV}')
