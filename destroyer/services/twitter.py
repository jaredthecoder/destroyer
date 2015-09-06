"""twitter.py - Module for Twitter service functionality"""

import time

import click
import tweepy

from ..settings import consumer_key, consumer_secret
from ..settings import access_token, access_token_secret


class TwitterDestroyer():
    """Destroyer class for Twitter integration.
    """
    def __init__(self, unfollow_non_followers=False):
        """Initializer method"""
        self.auth = tweepy.auth.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth_handler=self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        self.unfollow_non_followers = unfollow_non_followers
        self.logger = None

    def _unfollow(self, user):
        """Private method that takes a Tweepy user object and unfollows the user.
        The user that is unfollowing the user passed into this function is the user
        authenticated with the current Tweepy API class instance."""
        print('Unfollowing ' + str(user.id).rjust(10))
        try:
            user.unfollow()
        except:
            print('  .. failed, sleeping for 5 seconds and then trying again.')
            time.sleep(5)
            user.unfollow()
        print(' .. completed, sleeping for 1 second.')
        time.sleep(1)

    def destroy(self):
        """Public method that implements the abstracted functionality of unfollowing users"""
        if self.unfollow_non_followers:
            followers = dict()
            print('Getting followers')
            for follower in tweepy.Cursor(self.api.followers).items():
                followers[follower.id] = follower
            print('Finished getting followers')

        friends = dict()
        print('Getting friends')
        for i, friend_set in enumerate(tweepy.Cursor(self.api.friends, count=500).pages()):
            for friend in friend_set:
                print(friend.screen_name)
                friends[friend.id] = friend
        print('Finished getting friends')

        if self.unfollow_non_followers:
            non_friends = [friend for friend in friend_objects if friend.id not in followers]

        if self.unfollow_non_followers:
            answer = click.confirm('Are you sure you want to unfollow all the people you are following that are not following you? [Y/n]', abort=True)
            for non_friend in non_friends:
                self.unfollow(non_friend)
        else:
            for friend in friends:
                answer = click.confirm('Do you want to unfollow your friend, {friend}? [Y/n]'
                                        .format(friend=str(friend.id).rjust(10)))
                if not answer:
                    print('Okay, not unfollowing {friend}'.format(friend=str(friend.id)).rjust(10))
                    continue
                print('Unfollowing ' + str(friend.id).rjust(10))
                self._unfollow(friend)
