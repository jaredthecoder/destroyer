"""twitter.py - Module for Twitter service functionality"""

import time

import tweepy

from ..settings import consumer_key, consumer_secret
from ..settings import access_token, access_token_secret


class TwitterDestroyer():
    def __init__(self, unfollow_non_followers=False):
        self.auth = tweepy.auth.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth_handler=self.auth)

        self.unfollow_non_followers = unfollow_non_followers
        self.logger = None

    def _unfollow(self, user):
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
        if self.unfollow_non_followers:
            follower_objects = [follower for follower in tweepy.Cursor(self.api.followers).items()]
            followers = dict([(follower.id, follower) for follower in follower_objects])

        friend_objects = [friend for friend in tweepy.Cursor(self.api.friends).items()]
        friends = dict([(friend.id, friend) for friend in friend_objects])

        if self.unfollow_non_followers:
            non_friends = [friend for friend in friend_objects if friend.id not in followers]

        if self.unfollow_non_followers:
            answer = raw_input('Are you sure you want to unfollow all the people you are following that are not following you? [Y/n]').lower()
            if answer and answer[0] != 'y':
                return True
            for non_friend in non_friends:
                self.unfollow(non_friend)
        else:
            for friend in friends:
                answer = raw_input('Do you want to unfollow your friend, {friend}? [Y/n]'
                                    .format(friend=str(friend.id).rjust(10))).lower()
                if answer and answer[0] != 'y':
                    print('Okay, not unfollowing {friend}'.format(friend=str(friend.id)).rjust(10))
                print('Unfollowing ' + str(friend.id).rjust(10))
                self._unfollow(friend)
