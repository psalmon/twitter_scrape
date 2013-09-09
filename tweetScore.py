#print all "text" values
from twython import Twython
from pymongo import MongoClient
from pprint import pprint
import nltk
from nltk.corpus import stopwords #strip words which have little meaning


client = MongoClient('localhost', 27017)
db = client.twitter #db
tweets = db.tweets #tweets collection within twitter db

tweetCursor = tweets.find({}, {"_id":False, "statuses.text":1}) ###########subdocument!!!

for doc in tweetCursor:
    pprint(doc["statuses"])#pass one by one to our sentiment analyzer