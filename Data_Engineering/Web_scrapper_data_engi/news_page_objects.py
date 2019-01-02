import bs4
import requests

from common import config

class HomePage:
    def __init__(sefl, news_site_uid, url):
        self._config = config()['new_sites'][new_site_uid]
        self._queries = self._config['queries']
        self._html = None

        self._visit(url)

        def _visit(self, url):
            response = requests.get(url)
            response.raise_for_status()
            self._html = bs4.BeautifulSoup(response.text, 'html.parser')
        


