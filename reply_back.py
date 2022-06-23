#!/usr/bin/env python
# reply_back.py

from venv import create
from webbrowser import get
from authenticate_twitter import create_api, auth_client
import tweepy
import time

def check_tweet_mentions(api,client, keyword, since):
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id != None:
            continue
        if keyword.lower() in tweet.text.lower():
            print('Replying to user')
            if not tweet.user.following:
                try:
                    client.follow_user(tweet.user.id)
                except:
                    print("You can't follow yourself lol")
            
            user = api.get_user(user_id=tweet.user.id)
            screen_name = user.screen_name
            client.create_tweet(text="Thanks for getting in touch @"+screen_name+" :)",in_reply_to_tweet_id=tweet.id)
    return new_since_id




api = create_api()
client = auth_client()

since_id = 1
while True:
    since_id = check_tweet_mentions(api,client, 'Chris', since_id)
    time.sleep(60)
