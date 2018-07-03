import glob
from bs4 import BeautifulSoup
from config import ROOT_PATH


class GetDbVersionParser:

    def __init__(self, crawled_site, storage_adapter):
        self.crawled_site = crawled_site
        self.storage_adapter = storage_adapter

    def get_db_version(self):
        payloads = {}
        for file_path in glob.glob('%s/crawler_outputs/%s-*-get-db-version.html' %
                                  (ROOT_PATH, self.crawled_site)):
            content = self.storage_adapter.get(file_path)
            payloads[file_path] = content

        for key, value in payloads.items():
            soup = BeautifulSoup(value, 'html.parser')
            for tag in soup.findAll('pre'):
                _, __, surname_field = tag.prettify().split('<br/>')
                if self.has_numbers(surname_field):
                    db_version = surname_field\
                        .replace('Surname: ', '').replace('</pre>', '').strip()
                    return db_version

    def has_numbers(self, input):
        return any(char.isdigit() for char in input)
