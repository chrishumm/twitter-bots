#!/usr/bin/env python
# reply_back.py

from venv import create
from webbrowser import get
from authenticate_twitter import create_api, auth_client
import tweepy
import time
import random

reply_phrases = ['Thanks for getting in touch with us @', 'Great to hear from you @', 'Nice hearing from you @', 'Thanks for leaving us a message @']
replied = [] 


def check_tweet_mentions(api,client, keyword, since):
    new_since_id = since_id
    test = tweepy.Cursor(api.mentions_timeline,since_id=since_id).items()
    for tweet in tweepy.Cursor(api.mentions_timeline,since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id != None:
            continue
        if keyword.lower() in tweet.text.lower():
            print('Replying to user')
            if(check_tweet_replied(tweet.id) == False):
                if not tweet.user.following:
                    try:
                        client.follow_user(tweet.user.id)
                    except:
                        print("You can't follow yourself lol")
                
                user = api.get_user(user_id=tweet.user.id)
                screen_name = user.screen_name
                tweeted_phrase = random.choice(reply_phrases)
                client.create_tweet(text=tweeted_phrase+screen_name+" :)",in_reply_to_tweet_id=tweet.id)
                replied.append(tweet.id)
    return new_since_id

def check_tweet_replied(id):
    id = str(id)
    try:
        with open('replied_tweets.txt','r') as replied_tweets_file:
            replied = replied_tweets_file.readlines()
            for i, value in enumerate(replied):
                replied[i] = replied[i].strip('\n')
            replied_tweets_file.close()
    except:
        with open('replied_tweets.txt','w') as replied_tweets_file:
            replied_tweets_file.write(id +'\n')
            replied_tweets_file.close()
            return False
    if(id not in replied):
        with open('replied_tweets.txt','a') as replied_tweets_file:
            replied_tweets_file.write(id +'\n')
            replied_tweets_file.close()
        return False
    else:
        return True



api = create_api()
client = auth_client()

since_id = 1
keyword = '@chrishumm_'
check_count = 10
for i in range(check_count): #only checks x times
    since_id = check_tweet_mentions(api,client, keyword, since_id)
    time.sleep(60)
