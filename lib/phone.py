from bs4 import BeautifulSoup
from lib.validacao import Validacao
import requests
import re


class FindUrls:

    def __init__(self, url):
        self.url = url

    def find_phone(self):

        if Validacao.valid_url(self):
            urls = self
        else:
            urls = 'http://' + self
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.89 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        }
        html = requests.get(urls, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        texto = soup.text
        regex = re.compile(r'((?:\+?\d{1,4})?\s(?:\(?\d{2,4}\)?)\s(?:\d{2,5})(?:\-|\s)?(?:\d{2,4})(?:\-\d{2})?)')
        phones = regex.findall(texto)
        p = []
        for phone in phones:
            ph = phone.replace('-', ' ')
            if len(ph) > 10:
                p.append(ph)
        return p

    def find_img(self):

        if Validacao.valid_url(self):
            urls = self
        else:
            urls = 'http://' + self
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.89 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        }
        html = requests.get(urls, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        for src in soup.find_all('img'):
            r = src.get('src')
            if re.findall(r'[lL]ogo', r):
                return r
            else:
                return r

    def json(self):
        phone = FindUrls.find_phone(self)
        img = FindUrls.find_img(self)
        return print({
            'website': self,
            'logo': img,
            'phone': phone
        })