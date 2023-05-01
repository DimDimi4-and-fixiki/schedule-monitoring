import click
import uvicorn

from config import HOST, PORT


@click.group()
def cli():  # pragma: no cover
    pass


@cli.command()
def run_server():  # pragma: no cover
    uvicorn.run('commands.run_server:main_app', host=HOST, port=PORT, log_level='info', reload=True)


if __name__ == '__main__':
    cli()
