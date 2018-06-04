#the code fetches the twitter stream for track filter 
import tweepy
from tweepy import OAuthHandler
import json
from tweepy.streaming import StreamListener
from tweepy import Stream

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
tweet_api = tweepy.API(auth)

class Mylistener(StreamListener):
    def on_data(self,data):
        print(data)
        return True
    def on_error(self, status):
        print (status)

twitstream = Stream(auth, Mylistener())
twitstream.filter(track=["narendra", "modi"])