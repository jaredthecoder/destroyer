"""destroyer.py - Main module file for the application. Includes the code for
the command line interface."""


import click

from .services.twitter import TwitterDestroyer
from .services.facebook import FacebookDestroyer


@click.group()
def cli():
    pass


@click.command()
@click.option('--unfollow_nonfollowers', default=False, type=click.BOOL)
def twitter(unfollow_nonfollowers):
    twitter_destroyer = TwitterDestroyer(unfollow_nonfollowers)
    twitter_destroyer.destroy()


@click.command()
def facebook():
    facebook_destroyer = FacebookDestroyer()
    facebook_destroyer.destroy()


def main():
    cli.add_command(twitter)
    cli.add_command(facebook)
    cli()
