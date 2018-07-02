import glob
from bs4 import BeautifulSoup
from config import ROOT_PATH


class GetDbUsersParser:

    def __init__(self, crawled_site):
        self.crawled_site = crawled_site

    def get_db_usernames(self):
        payloads = {}
        for filename in glob.glob('%s/crawler_outputs/%s-*-get-db-users.html' %
                                  (ROOT_PATH, self.crawled_site)):
            content = self.get_payload(filename)
            payloads[filename] = content

        db_usernames = {}
        for key, value in payloads.items():
            soup = BeautifulSoup(value, 'html.parser')
            usernames = []
            for tag in soup.findAll('pre'):
                _, firstname_field, surname_field = tag.prettify().split('<br/>')
                firstname = firstname_field.replace('First name: ', '')
                surname = surname_field.replace('Surname: ', '').replace('</pre>', '').strip()
                full_name = '%s, %s' % (firstname, surname)
                usernames.append(full_name)
            db_usernames[key.replace(ROOT_PATH, '')] = usernames

        return db_usernames

    def get_payload(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()
