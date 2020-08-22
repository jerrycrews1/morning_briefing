import datetime
import requests
from bs4 import BeautifulSoup


def get_today_reading():
    year = str(datetime.datetime.now().year)[:2]
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    if len(day) < 2:
        day = str(0) + day
    if len(month) < 2:
        month = str(0) + month
    url = f'http://www.usccb.org/bible/readings/{month}{day}{year}.cfm'
    webpage = requests.get(url)
    webpage_content = webpage.content
    soup = BeautifulSoup(webpage_content, 'html.parser')
    # reading_titles = [i.getText() for i in soup.select('.bibleReadingsWrapper > h4')]
    # reading_text = [i for i in soup.select('.bibleReadingsWrapper > .poetry')]
    reading_titles = [i.getText() for i in soup.select('.content-header > h3')]
    reading_text = [i for i in soup.select('.content-body')]
    readings = dict(zip(reading_titles, reading_text))
    return readings


# print(get_today_reading())
