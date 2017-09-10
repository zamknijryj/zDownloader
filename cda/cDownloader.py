# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json


class cDownloader():
    def __init__(self):
        self.base = 'ebd.cda.pl/615x344/'

    def getCdaDownloadLink(self, url):
        #url = 'https://www.cda.pl/video/60597053?wersja=1080p'
        response = requests.get(url).content
        soup = BeautifulSoup(response, 'html.parser')

        base = 'ebd.cda.pl/615x344/'

        x = url.rsplit("?wersja", 1)[0]
        number = x.split("video/", 1)[1]

        media = 'mediaplayer'

        link = 'http://' + base + number

        response2 = requests.get(link).content
        soup2 = BeautifulSoup(response2, 'html.parser')

        div = soup2.find('div', {'id': media + number})
        data = json.loads(div['player_data'])

        download = data['video']['file']
        return download
        # 'http://vrbx072.cda.pl/dYXEHM8Nw3y_TZTmTs4e0g/1500496486/vl9afb2190473cc908d0c33cdb15bb212994083ca30c797154058bc8717c4ca746.mp4'
