import datetime
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# for loading the .env file
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv("SP_EMAIL")
PASSWORD = os.getenv("SP_PASSWORD")


def get_sp_wod():
    """Retrieves the current day's Street Parking WOD from Wodify"""

    chrome_options = Options()
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # EC2 Driver
    # driver = webdriver.Chrome(options=chrome_options)
    # https://medium.com/@praneeth.jm/running-chromedriver-and-selenium-in-python-on-an-aws-ec2-instance-2fb4ad633bb5

    # This driver is for MacOS.  NOT EC2
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    driver.get('https://app.wodify.com/')
    sleep(5)
    driver.find_element_by_xpath('//*[@id="Input_UserName"]').send_keys(EMAIL)
    driver.find_element_by_xpath(
        '//*[@id="Input_Password"]').send_keys(PASSWORD)
    driver.find_element_by_xpath(
        '//*[@id="FormLogin"]/div[2]/div[5]/button').click()
    sleep(2)

    wod_comment = driver.find_element_by_xpath(
        '//*[@id="AthleteTheme_wtLayoutNormal_block_wtMainContent_WOD_UI_wt9_block_wtWODWrapper"]/div[2]')
    fullstring = wod_comment.text.lower()
    substring = "no program b"
    # if there is no program b, go to a
    if substring in fullstring:
        driver.find_element_by_xpath(
            '//*[@id="AthleteTheme_wtLayoutNormal_block_wtSubNavigation_wtcbDate"]').click()
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="AthleteTheme_wtLayoutNormal_block_wtSubNavigation_wtcbDate"]/option[3]').click()
        sleep(1)
    wod = driver.find_element_by_xpath(
        '//*[@id="AthleteTheme_wtLayoutNormal_block_wtMainContent_WOD_UI_wt9_block_wtWODWrapper"]')

    return wod.get_attribute('innerHTML')


def get_crossfit_wod():
    """Retrieves the current day's WOD from the official Crossfit website"""

    year = str(datetime.datetime.now().year)[:2]
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    if len(day) < 2:
        day = str(0) + day
    if len(month) < 2:
        month = str(0) + month
    date_in_crossfit_format = f"{year}{month}{day}"
    url = f'https://www.crossfit.com/{date_in_crossfit_format}'
    webpage = requests.get(url)
    webpage_content = webpage.content
    soup = BeautifulSoup(webpage_content, 'html.parser')
    wod = soup.select('div > article')[0]
    return wod
