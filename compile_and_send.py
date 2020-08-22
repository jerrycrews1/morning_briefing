from date import get_date
from news import get_news
from wod import get_sp_wod
from weather import get_today_weather
from daily_readings import get_today_reading
from twitter_trending import twitter_trending

from send_email import send_email

def compile_and_send():
    var_dicts = dict()
    var_dicts['date'] = get_date()
    var_dicts['wod'] = get_sp_wod()
    var_dicts['readings'] = get_today_reading()
    var_dicts['trends'] = twitter_trending(2514815)
    var_dicts['articles'] = get_news()
    var_dicts['weather'] = get_today_weather("22003")
    send_email(var_dicts)


compile_and_send()
