from twython import Twython
from pymongo import MongoClient

#mongoDB API
client = MongoClient('localhost', 27017)
db = client.twitter #db
tweets = db.tweets #tweets collection within twitter db

#twitter API
api = "https://api.twitter.com/1.1/search/tweets.json?q="
query = "twython"
APP_KEY = "x"
APP_SECRET = "x"
OAUTH_TOKEN = "x"
OAUTH_TOKEN_SECRET = "x"
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def searchTweets(query):
    resp = twitter.request(api+query)
    return (resp)

response = (searchTweets(query))
tweets.insert(response)

#Try: find last time, modify search to get next 15 most recent since that time.
#exception: if we got the rate limit error, pause for designated time
#if count returned is zero, pause for certain amount of time


