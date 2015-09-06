"""facebook.py - Module for Facebook service functionality"""

import time

import click
from facepy import GraphAPI

from ..settings import facebook_access_token


class FacebookDestroyer():
    """Destroyer class for Facebook integration.
    """
    def __init__(self):
        """Initializer method"""
        self.graph = GraphAPI(facebook_access_token)

        self.logger = None

    def _unfriend(self):
        """Private method that takes a Facebook friend object and unfriends them.
        NOTE: At the moment, Facebook does NOT let you unfriend users programatically.
        Therefore, this functionality does not work.
        """
        pass

    def destroy(self):
        """Public method that implements the abstracted functionality of unfriending users"""
        # graph.get('me/friend_list')
        pass
