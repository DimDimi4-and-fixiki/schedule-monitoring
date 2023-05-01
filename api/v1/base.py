from fastapi import APIRouter

from common.utils import get_current_platform

api_v1 = APIRouter(
    prefix='/api/v1',
    tags=['api_v1'],
    dependencies=[],
)


@api_v1.get('/ping')
async def ping() -> str:
    return 'pong from api_v1'


@api_v1.get('/get_platform')
def get_platform() -> str:
    return str(get_current_platform().value)
