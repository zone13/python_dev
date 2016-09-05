#!/usr/bin/env python

#Python script to retrive the latest tweet from a user
#Created by zone13.io (https://www.zone13.io)
#Version 1.0
#Usage - ./script.py <twitter_handle>
#e.g. ./script.py rihanna
#Adapted from https://github.com/bear/python-twitter

#Requirement - pip install python-twitter

import sys,twitter

api = twitter.Api()

#Populate your twitter API details below

consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

api = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token_key,
    access_token_secret=access_token_secret
)

def user_tweet(thandle):
	statuses = api.GetUserTimeline(screen_name=thandle)
	return statuses[0].text
	
if __name__ == "__main__":
	latest_tweet = user_tweet(sys.argv[1])
	print latest_tweet
