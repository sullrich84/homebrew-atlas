import click


@click.command()
@click.option("--version", "-v", is_flag=True, help="Display the version.")
def main():
    click.echo(f"Atlas version xx")


def cli():
    print("atlas/cli.py:cli()")


if __name__ == "__main__":
    cli()
