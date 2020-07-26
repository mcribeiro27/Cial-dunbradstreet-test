import re


class Validacao:

    def __init__(self, url):
        self.url = url

    def valid_url(self):
        regex = re.compile(r'(https?://(?:\w{3}\.)?[a-z0-9]+\.[a-z0-9]+(?:\.[a-z]+)?)')
        urls = regex.findall(self)
        if urls:
            return True
        else:
            return False
