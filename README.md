![TwitterBotsTITLE](https://github.com/chrishumm/twitter-bots/blob/28a2970f11be6b97caf71fd0f1230434c6fc22aa/twitterbots.png)

# TwitterBots

Here is a collection of my bots written for Twitter. You can view the [repository](https://github.com/chrishumm/twitter-bots) over on my [Github :)](https://www.github.com/chrishumm). They are all written in Python and use the Tweepy library for twitter integration.
All the bots below require the use of authenticate_twitter.py. You need to provide your own auth.txt and bearer_token txt files.
The format of the files are:

~~~js
// file: "auth.txt"
<customer token>
<customer token secret>
<access token>
<access token secret>
~~~

~~~js
// file: "bearer_token.txt"
<bearer_token>
~~~

My Stoic Quote bot runs on AWS Lambda and tweets random quotes at a daily interval, complete with hashtags and doesn't repeat itself.

My reply_back bot replies back to mentions @ your username. You can modify it to scan for certain keywords and reply back. This also ran on AWS Lambda, but no longer does. (I'm not that popular!)

The retweet_bot checks for tweets that match certain keywords, favourites them and then retweets them. You can customise it to your needs.

My followfollowers bot automatically scans through your follower feed and follows back anyone you're not currently following. 

The versions uploaded to AWS slightly differ from the versions you can run on your computer. This is due to AWS Lambda needing to use s3 buckets to write files.

# Features

- Integrates with twitter to automate tweets/ automate replies

# TODO

- Add an AI chatbot

# Getting Started

Clone the repo and start running locally. You need to have a Twitter developer account and add your own credentials.

## Installing from source (Local)

### System Requirements

:bulb: Before you begin, make sure you have all the below installed:

- An editor
- Twitter Developer account
- Python
- 
# Alpha Version

I'm constantly adding more things, but it isn't completely finished yet.
# Support

## Contact me
You can contact me directly and I will try to get around to sorting out the numerous bugs. 

## Create a bug report

If you see an error message or run into an issue, please [create bug report](https://github.com/chrishumm/twitter-bots/issues/new?assignees=&labels=type%3A%20bug&template=bug_report.md&title=). 


## Submit a feature request

If you have an idea, or you're missing a capability that would make development easier and more robust, please [Submit feature request](https://github.com/chrishumm/twitter-bots/issues/new?assignees=&labels=type%3A%20feature%20request&template=feature_request.md&title=).
I am still working on this from time to time for fun.

# Contributing

Please message me privately if you want to contribute.

# Contributors ✨

- Me, Myself and I
