import click


@click.group()
@click.version_option()
def cli():
    "Demo of simonw/click-app-template-repository"


@cli.command(name="command")
@click.argument(
    "example"
)
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")
