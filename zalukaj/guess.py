from bs4 import BeautifulSoup
import requests
import re


class zDownloader():

    def __init__(self):
        self.base = 'https://zalukaj.com'

    def getDownloadLink(self, url):
        response = requests.get(url).content
        soup = BeautifulSoup(response, 'html.parser')

        for frame in soup.find_all('iframe'):
            urlTo2Link = frame['src']

        url2 = self.base + urlTo2Link

        response2 = requests.get(url2).content
        soup2 = BeautifulSoup(response2, 'html.parser')

        for a in soup2.find_all('a', href=True):
            link = a['href']

        url3 = self.base + link

        response3 = requests.get(url3).content
        soup3 = BeautifulSoup(response3, 'html.parser')

        for frame in soup3.find_all('iframe'):
            link2 = frame['src']

        link2 = link2[2:]

        linkFinal = link2.split('/width-470/height-305/', 1)[0]
        linkFinal = linkFinal[:10] + 'd' + linkFinal[11:]
        linkFinal = 'http://' + linkFinal

        response4 = requests.get(linkFinal).content
        soup4 = BeautifulSoup(response4, 'html.parser')

        scripts = soup4.find_all('script', {'type': 'text/javascript'})

        download = re.search(r"<a [^>]*?(href=\"([^\">]+))",
                             scripts[2].text)[1]
        downloadLink = re.sub('href="http://', '', download)
        return downloadLink

    def zmienne(self):
        self.odc = []
        self.links = []

    def getSeriesDownloadLink(self, url):

        # link = "https://zalukaj.com/kategoria-serialu/2348,1/arrow_arrow_sezon_4/"
        response = requests.get(url).content
        soup = BeautifulSoup(response, 'html.parser')

        self.zmienne()

        productDivs = soup.findAll('div', attrs={'id': 'sezony'})

        for div in productDivs:
            linki = div.find('a')['href'][2::]
            odcinki = div.find('a')['title']
            self.odc.append(odcinki)
            self.links.append(linki)
            # print("%s = %s" % (odcinki, linki))

        #print("Możliwe odcinki: ")
        #i = 0
        # for odcinek in self.odc:
        #    i += 1
        #    print(str(i) + ")", odcinek)

        #episode = int(input("Podaj liczbe przy odcinku: "))
        # odcinek = self.odc[episode - 1], "=", self.links[episode - 1]
        # odcinek = self.links[episode - 1]
