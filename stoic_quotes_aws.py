#!/usr/bin/env python
# stoic_quotes.py

import random
from webbrowser import get
from authenticate_twitter import create_api, auth_client
import tweepy
import time
import re
import boto3

def shuffle_old_quotes():
    old_quotes = []
    with open ("stoic_quotes.txt",'w') as new_quote_file:
        with open("tweeted_stoic_quotes.txt", 'r') as old_quote_file:
            old_quotes = old_quote_file.readlines()
            old_quote_file.close()
        with open("tweeted_stoic_quotes.txt", 'w') as old_quote_file:
            old_quote_file.write("")
            old_quote_file.close()

        for i, value in enumerate(old_quotes):
            new_quote_file.write(old_quotes[i])

        new_quote_file.close()

def read_quotes():
    print('readfromfile')
    s3_client = boto3.client('s3')
    s3_client.download_file('stoicquotes-chrishumm', 'stoic_quotes.txt', '/tmp/stoic_quotes.txt')
    s3_client.download_file('stoicquotes-chrishumm', 'tweeted_stoic_quotes.txt', '/tmp/tweeted_stoic_quotes.txt')

    try:
        with open ("/tmp/stoic_quotes.txt",'r') as quotes:
             list_of_quotes = quotes.readlines()
             number_of_quotes = len(list_of_quotes)
             if number_of_quotes == 0:
                shuffle_old_quotes()
                return read_quotes()

        quotes.close()
    except(FileNotFoundError):
            print("File does not exist")

    return list_of_quotes

def random_quote(list_of_quotes):
    random.shuffle(list_of_quotes)
    #check for previous quotes?
    quote = list_of_quotes[0]
    quote_search = re.compile(quote)
    line_number = None
    s3_client = boto3.client('s3')
    with open ("/tmp/stoic_quotes.txt",'r') as quotes:
        test_file = quotes.readlines()
        quotes.close()
        for i, value in enumerate(test_file):
            if(quote_search.search(test_file[i]) != None):
                line_number = i
                with open ("/tmp/stoic_quotes.txt",'w') as remove_quote:
                
                    del test_file[i]
                    for removed_quote in test_file:
                        remove_quote.write(removed_quote)
                    
                    remove_quote.close()
                    
                    s3_client.upload_file('/tmp/stoic_quotes.txt', 'stoicquotes-chrishumm', 'replied_tweets.txt')


                try:
                    with open("/tmp/tweeted_stoic_quotes.txt", 'a') as tweeted_quote:
                          tweeted_quote.write(quote)
                          tweeted_quote.close()

                          s3_client.upload_file('/tmp/tweeted_stoic_quotes.txt', 'stoicquotes-chrishumm', 'tweeted_stoic_quotes.txt')

                except:
                    with open("/tmp/tweeted_stoic_quotes.txt", 'w') as tweeted_quote:
                    
                        for quote in test_file:
                            tweeted_quote.write(quote)
                        
                        tweeted_quote.close()
                        s3_client.upload_file('/tmp/tweeted_stoic_quotes.txt', 'stoicquotes-chrishumm', 'tweeted_stoic_quotes.txt')

                break
        




    quote.strip('\n')
    return quote
    print("Choose a random quote")

def tweet_quotes(client, quote):
    tweet_char_limit = 280
    hashtags = "#stoicism"

    tweet_length = len(quote+hashtags)
    print("tweet quote")
    if tweet_length < tweet_char_limit:
        client.create_tweet(text=quote + hashtags)
        return True
    else:
        print("Tweet is too long!")
        return False





def lambda_handler(event, context):
    api = create_api()
    client = auth_client()
    quotes = read_quotes()
    chosen_quote = random_quote(quotes)
    if(tweet_quotes(client,chosen_quote) == True):
        quit()
    else:
        exit()