#!/user/bin/env python3
import requests
from bs4 import BeautifulSoup
from jinja2 import Template


def getPrayerTimes(url):

    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')
    rows = soup.find_all('tbody')
    return rows[0]

def getWeather(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'html.parser')
    temp = soup.find_all("span", class_="wxo-metric-hide")[1]
    return temp
