from venv import create
from authenticate_twitter import create_api, get_bearer_token
import tweepy
import time

class tweet_printer(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        print(tweet.text)
        status = api.get_status(tweet.id) 
        favorited = status.favorited  
        retweeted = status.retweeted

        if tweet.in_reply_to_user_id != None:
            # This tweet is a reply or I'm its author so, ignore it
            print("Test its me ")
            return
        if favorited == False:
            try:
                print("i havent favourited it ")
               # tweet.favorite()
            except Exception as e:
                print("error")
        if retweeted == False:
            # Retweet, since we have not retweeted it yet
            try:
                print("I havent retweeted")
                api.retweet(tweet.id)
            except Exception as e:
                print("error")


api = create_api()
streaming_client = tweet_printer(get_bearer_token())
streaming_client.add_rules(tweepy.StreamRule('Python'))
streaming_client.filter()
