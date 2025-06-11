import commands as cmds
import click

@click.group
def cli() -> None:
	pass

cli.add_command(cmds.init)
cli.add_command(cmds.register)