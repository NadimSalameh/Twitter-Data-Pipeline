import pymongo
import time
from sqlalchemy import create_engine
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyser = SentimentIntensityAnalyzer()
# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

time.sleep(10)  # seconds

# Select the database you want to use withing the MongoDB server
db = client.twitter

pg = create_engine('postgresql://docker_user:1234@postgresdb:5432/twitter', echo=True)
pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500) UNIQUE ,
    
    sentiment NUMERIC
);
''')
mentions_regex= '@[A-Za-z0-9_]+' #pattern to remove all @ mentions in the tweet
url_regex='https?:\/\/\S+' #Pattern to remove all URL's
hashtag_regex= '#' # pattern to remove  hashtag
rt_regex= 'RT\s' # pattern to remove all retweets ie. RT

def clean_tweets(tweet):
    tweet = re.sub(mentions_regex, '', tweet)  #removes @mentions
    tweet = re.sub(hashtag_regex, '', tweet) #removes hashtag symbol
    tweet = re.sub(rt_regex, '', tweet) #removes RT to announce retweet
    tweet = re.sub(url_regex, '', tweet) #removes most URLs
    
    return tweet

docs = db.tweets.find()
for doc in docs:
    print(doc)
    text = clean_tweets(doc['text'])
    score = analyser.polarity_scores(text)['compound'] # placeholder value
    query = "INSERT INTO tweets VALUES (%s, %s) ON CONFLICT DO NOTHING;"
    pg.execute(query, (text, score))

