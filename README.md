IN DOCKER PIPELINE TWITTER :


- Create and manage a pipeline of data that is streaming, i.e. real-time.

- Data source for this project is the Twitter API.


******************

Register your application on apps.twitter.com.

Navigate to the Twitter App dashboard and open the Twitter App for which you would like to generate access tokens.

Navigate to the “keys and tokens” page.

You’ll find the API keys, user Access Tokens, and Bearer Token on this page.

Write down the Bearer Token.

****************

pip install tweepy==4.4.0

***************

Install Docker

**************

Use docker-compose to orchestrate a data pipeline with five containers:

tweet_collector    self-made       collects tweets and stores them in MongoDB

mongodb             mongo          stores tweets as JSON documents

etl_job           self-made        analyzes sentiment of tweets from MongoDB and stores them in PostgreSQL

postgresdb        postgres         stores tweets and annotation in a table

slack_bot        self-made         publishes highly ranking tweets in a Slack channel

*****************

ETL : Extract - Transform - Load.

use ETL to  Extract data from MongoDB then Transform(performs the Sentiment Analysis and returns entries with sentiment),
and finally Load it to PostgresDB


***********

Create new app in Slack Bot

Connect the script to the PostgreSQL container

write the Python script to post a message once an hour 
******


