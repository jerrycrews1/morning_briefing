from newsapi import NewsApiClient
import os
from dotenv import load_dotenv
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_news():
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    top_headlines = newsapi.get_top_headlines(sources='fox-news')
    return top_headlines['articles']