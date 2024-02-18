import os
import click
from atlas.version import __version__


@click.command()
@click.option("--username", prompt=True, default=lambda: os.environ.get("USER", ""))
def hello(username):
    click.echo(f"Hello, {username}!")


def cli():
    print(f"atlas {__version__}")


if __name__ == "__main__":
    cli()
