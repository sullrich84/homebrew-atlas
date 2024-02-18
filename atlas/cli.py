# import click
from atlas.version import __version__


def cli():
    print(f"atlas {__version__}")


if __name__ == "__main__":
    cli()
