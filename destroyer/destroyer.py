"""destroyer.py - Main module file for the application. Includes the code for
the command line interface."""


import click

from services.twitter import TwitterDestroyer

@click.command()
def cli():
    click.echo('I am Destroyer, harbinger of exiled followers, friends, and more.')


def main()
    cli()
