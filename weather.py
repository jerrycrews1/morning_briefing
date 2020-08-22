import requests
import os
from dotenv import load_dotenv
load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def get_today_weather(zip_code):
    response = requests.get(
        f'https://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={zip_code}&days=2')
    data = response.json()
    high_temp = data['forecast']['forecastday'][0]['day']['maxtemp_f']
    low_temp = data['forecast']['forecastday'][0]['day']['mintemp_f']
    description = data['forecast']['forecastday'][0]['day']['condition']['text'].lower()
    city_name = data['location']['name']
    inside_message = f'Today in {city_name} the weather is {description} with a high of {round(high_temp)}' \
                     f'\N{DEGREE SIGN}F and a low of {round(low_temp)}\N{DEGREE SIGN}F'
    return inside_message

# print(get_today_weather("22003"))