import requests
from bs4 import BeautifulSoup

base = 'https://www.zalukaj.com'
url = 'https://zalukaj.com/zalukaj-film/24762/legion_samob_jc_w_suicide_squad_2016_.html'

response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')

for frame in soup.find_all('iframe'):
    urlTo2Link = frame['src']

url2 = base + urlTo2Link

response2 = requests.get(url2).content
soup2 = BeautifulSoup(response2, 'html.parser')

for a in soup2.find_all('a', href=True):
    link = a['href']

url3 = base + link
response = requests.get(url3).content
soup3 = BeautifulSoup(response, 'html.parser')


linki = []
for a in soup3.find_all('a', href=True):
    link3 = a['href']
    linki.append(link3)

print(linki)
