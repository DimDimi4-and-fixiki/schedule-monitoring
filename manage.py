import click

from commands.mos_ru import run_mos_ru_monitoring


@click.group()
def cli():  # pragma: no cover
    pass


@cli.command()
def mos_ru_monitoring():  # pragma: no cover
    run_mos_ru_monitoring()


if __name__ == '__main__':
    cli()
