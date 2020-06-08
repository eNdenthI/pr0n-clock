import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=34.20034000000004&lon=-119.18011999999999#.Xtu-Q0VKiUk')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
forecast = week.find_all(class_='tombstone-container')
items = {(items.find(class_='period-name').get_text()): (items.find(class_='short-desc').get_text()) for items in forecast}
# items = [items.find(class_='period-name').get_text() for items in forecast]
