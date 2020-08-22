import ssl
import tweepy


# for loading the .env file
import os
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

DC_WOEID = 2514815


def twitter_trending(woeid):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    results = api.trends_place(DC_WOEID)

    return results[0]['trends']

# print(twitter_trending(DC_WOEID))
