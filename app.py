from fastapi import FastAPI
from starlette.responses import RedirectResponse

from config import APPLICATION_NAME

application = FastAPI(
    title=APPLICATION_NAME,
)


@application.get('/ping')
async def ping() -> str:  # pragma: no cover
    return 'pong from app'


@application.get('/', include_in_schema=False)
async def redirect_to_docs() -> RedirectResponse:  # pragma: no cover
    response = RedirectResponse(url='/docs')
    return response


def include_routers(app: FastAPI) -> None:
    from api.v1.base import api_v1

    app.include_router(api_v1)


def build_app() -> FastAPI:
    include_routers(application)
    return application
