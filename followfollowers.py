#!/usr/bin/env python
# tweepy-bots/bots/followfollowers.py

from authenticate_twitter import create_api
import tweepy
import time


def check_followers(api):
    for follower in api.get_followers():
        if not follower.following:
            print('You are not following ' + follower.name)
        else:
            print('You are following ' + follower.name + ', congratulations!')

def main():
    api = create_api()
    while True:
        check_followers(api)
        time.sleep(60)

main()
