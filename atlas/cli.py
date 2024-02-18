import click 
from .version import __version__

@click.command()
@click.option("--version", "-v", is_flag=True, help="Display the version.")
def main():
        click.echo(f"Atlas version {__version__}")

def cli():
    print(f"atlas {__version__}")


if __name__ == "__main__":
    cli()
