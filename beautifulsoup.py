import requests
from bs4 import BeautifulSoup
import csv
import urllib

requests = requests.get(
    'https://www.pichunter.com/tags/Cum')
soup = BeautifulSoup(requests.content, 'html.parser')
soup = soup.find(class_='thumbtable')
img = soup.find_all('img')

src = []
for image in img:
    src.append(image["src"])

for i in range(len(src)):
    urllib.request.urlretrieve(src[i], str(i))
    print(src[i])


"""

with open('mycsv.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(src)

"""
