import glob
from bs4 import BeautifulSoup
from config import ROOT_PATH


class GetDbVersionParser:

    def __init__(self, crawled_site):
        self.crawled_site = crawled_site

    def get_db_version(self):
        payloads = {}
        for filename in glob.glob('%s/%s-*-get-db-version.html' %
                                  (ROOT_PATH, self.crawled_site)):
            content = self.get_payload(filename)
            payloads[filename] = content

        for key, value in payloads.items():
            soup = BeautifulSoup(value, 'html.parser')
            for tag in soup.findAll('pre'):
                _, __, surname_field = tag.prettify().split('<br/>')
                if self.has_numbers(surname_field):
                    db_version = surname_field\
                        .replace('Surname: ', '').replace('</pre>', '').strip()
                    return db_version

    def get_payload(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def has_numbers(self, input):
        return any(char.isdigit() for char in input)
