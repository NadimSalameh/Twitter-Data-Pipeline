from ssl import create_default_context
import time
from datetime import datetime
import logging
import random
import pymongo
import tweepy
import credentials
BEARER_TOKEN =credentials.BEARER_TOKEN
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    wait_on_rate_limit=True,
)



# Create a connection to the MongoDB database server
client_mongo = pymongo.MongoClient(host='mongodb') # hostname = servicename for docker-compose pipeline

# Create/use a database
db = client_mongo.twitter
# equivalent of CREATE DATABASE tweets;

# Define the collection
collection = db.tweets
# equivalent of CREATE TABLE tweet_data;


# What we actually want to do is to insert the tweet into MongoDB
search_query = "data science  -is:retweet -is:reply -is:quote lang:en -has:links"

cursor = tweepy.Paginator(
    method=client.search_recent_tweets,
    query=search_query,
    tweet_fields=['author_id', 'created_at', 'public_metrics'],
).flatten(limit=20)

for tweet in cursor:
    print(dict(tweet))# Insert the tweet into the collection

    logging.warning('-----Tweet being written into MongoDB-----')
    logging.warning(tweet)
    collection.insert_one(dict(tweet)) #equivalent of INSERT INTO tweet_data VALUES (....);
    logging.warning(str(datetime.now()))
    logging.warning('----------\n')

    time.sleep(3)

