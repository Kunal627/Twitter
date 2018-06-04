# this program will spit 20 status in json format for a user.

import tweepy
from tweepy import OAuthHandler
import json

days_old_min = 0
consumer_key = '8ZAYec97sgCkQCFHh6kfAkcbY'
consumer_secret = 'II1mS9Os3Kq5p9rfakGMawXaJmoYr9KNRyDlRnaviAvakll0N7'
access_token = '130534494-fETVtDzaR8ZgnNoY0qSISDxFNRZu0TY6mi4BY4Z5'
access_secret = 's7SZ0GejCHinCxXPWzR7SAVcOiyoxOClE4HGF56MBqsOT'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
tweet_api = tweepy.API(auth)

#for status in tweepy.Cursor(api.home_timeline).items(10):
#    # Process a single status
#    print(status.text)
def process_tweets(statuses):
    json_fmt = json.dumps(status._json)
    print(json_fmt)
#user_name = ['@narendramodi', '@rahulgandhi']
#for user in user_name:
#    print("Getting data for " + user)
#    item = tweet_api.get_user(user)
#    print("name: " + item.name)
#    print("screen_name: " + item.screen_name)
#    print("description: " + item.description)
#    print("statuses_count: " + str(item.statuses_count))
#    print("friends_count: " + str(item.friends_count))
#    print("followers_count: " + str(item.followers_count))
user_name = ['@narendramodi']
for user in user_name:
    for status in tweepy.Cursor(api.user_timeline, id=user).items(20):
        process_tweets(status)