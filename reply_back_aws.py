#!/usr/bin/env python
# reply_back.py

from venv import create
from webbrowser import get
from authenticate_twitter import create_api, auth_client
import tweepy
import time
import random
import boto3

reply_phrases = ['Thanks for getting in touch with us @', 'Great to hear from you @', 'Nice hearing from you @', 'Thanks for leaving us a message @']
replied = [] 


def check_tweet_mentions(api,client, keyword, since_id):
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id != None:
            continue
        if keyword.lower() in tweet.text.lower() and tweet.id not in replied:
            print('Replying to user')
            if(check_tweet_replied(tweet.id) == False):
                if not tweet.user.following:
                    try:
                        client.follow_user(tweet.user.id)
                    except:
                        print("You can't follow yourself")
                
                user = api.get_user(user_id=tweet.user.id)
                screen_name = user.screen_name
                tweeted_phrase = random.choice(reply_phrases)
                client.create_tweet(text=tweeted_phrase+screen_name+" :)",in_reply_to_tweet_id=tweet.id)
                replied.append(tweet.id)
    
def check_tweet_replied(id):
    id = str(id)
    s3_client = boto3.client('s3')
    s3_client.download_file('replyback-chrishumm', '<s3-bucket>', '/tmp/replied_tweets.txt')

    try:
        with open('/tmp/replied_tweets.txt','r') as replied_tweets_file:
            replied = replied_tweets_file.readlines()
            for i, value in enumerate(replied):
                replied[i] = replied[i].strip('\n')
            replied_tweets_file.close()
    except: #should never be called
        with open('/tmp/replied_tweets.txt','w') as replied_tweets_file:
            replied_tweets_file.write(id +'\n')
            replied_tweets_file.close()
            return False
    if(id not in replied):
        with open('/tmp/replied_tweets.txt','a') as replied_tweets_file:
            replied_tweets_file.write(id +'\n')
            replied_tweets_file.close()
            s3_client.upload_file('/tmp/replied_tweets.txt', '<s3-bucket>', 'replied_tweets.txt')
        return False
    else:
        return True

def lambda_handler(event, context):
    api = create_api()
    client = auth_client()
    since_id = 1
    keyword = 'Chris'
    check_count = 3
    for i in range(check_count): #only checks x times
        since_id = check_tweet_mentions(api,client, keyword, since_id)
        time.sleep(60)