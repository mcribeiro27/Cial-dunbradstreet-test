from bs4 import BeautifulSoup
import requests
import re


class FindUrls:

    def __init__(self, url):
        self.url = url

    def find_phone(self):
        html = requests.get(self)
        if html.status_code != 200:
            return None
        soup = BeautifulSoup(html.text, 'html.parser')
        texto = soup.text
        regex = re.compile(r'\(?\d{2,4}?\)?\s\d{3,5}\s\d{2,4}|'
                           r'\+?\d{1,3}?\s\(?\d{2,4}?\)?\s\d{3,5}-?\d{2,4}-\d{2}?|'
                           r'\(?\d{2,4}?\)?\s\d{3,5}-\d{2,4}')
        phones = regex.findall(texto)
        p = []
        for phone in phones:
            ph = phone.replace('-', ' ').strip()
            if len(ph) > 10:
                p.append(ph)
        return p

    def find_img(self):
        html = requests.get(self)
        if html.status_code != 200:
            return None
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
