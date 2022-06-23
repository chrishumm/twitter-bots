import tweepy
import sys
import logging
import os
import re

def get_bearer_token():
    try:
        with open('bearer_token.txt', 'r') as token_file:
            contents = token_file.readline()
            token_file.close()
    except(FileNotFoundError):
            print('Bearer token file not found')
            sys.exit()

    return contents

def auth_client():
    try:
        with open('auth.txt', 'r') as auth_file:
            contents = auth_file.readlines()
            auth_file.close()
    except(FileNotFoundError):
        print("Authentication credentials file was not found")
        sys.exit()

    for i, value in enumerate(contents):
        contents[i]= re.sub(r"\n", "", contents[i])

    test = re.sub(r"\n", "", contents[0])
    consumer_key = contents[0]
    consumer_secret = contents[1]
    access_token = contents[2]
    access_token_secret = contents[3]

    client = tweepy.Client(get_bearer_token(),consumer_key,consumer_secret,access_token,access_token_secret)
    return client
    
def create_api():
    try:
        with open('auth.txt', 'r') as auth_file:
            contents = auth_file.readlines()
            auth_file.close()
    except(FileNotFoundError):
        print("Authentication credentials file was not found")
        sys.exit()

    for i, value in enumerate(contents):
        contents[i]= re.sub(r"\n", "", contents[i])

    test = re.sub(r"\n", "", contents[0])
    consumer_key = contents[0]
    consumer_secret = contents[1]
    access_token = contents[2]
    access_token_secret = contents[3]

    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret,access_token, access_token_secret)    

    api = tweepy.API(auth,wait_on_rate_limit=True,retry_count=3)

    try:
        api.verify_credentials()
        print("Authentication Success")
        return api
    except:
        print("Authentication Error")
        sys.exit()