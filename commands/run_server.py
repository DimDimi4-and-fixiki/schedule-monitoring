from fastapi import FastAPI

from app import build_app


def main_app(*args, **kwargs) -> FastAPI:  # noqa
    app = build_app()

    return app
