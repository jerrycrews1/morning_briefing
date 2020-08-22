import calendar
import datetime


def get_date():
    day_of_week = calendar.day_name[datetime.datetime.today().weekday()]
    day_of_month = datetime.datetime.today().day
    month_of_year = calendar.month_name[datetime.datetime.today().month]
    year = datetime.datetime.today().year
    date_info = f'{day_of_week}, {day_of_month} {month_of_year} {year}'
    return date_info
