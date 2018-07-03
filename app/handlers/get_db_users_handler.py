import json
import scrapydo
from app.handlers.base_handler import BaseHandler
from app.storage.file_adapter import FileAdapter
from app.parsers.get_db_users import GetDbUsersParser
from config import DVWA_CRAWLER_SETTINGS

scrapydo.setup()


class GetDbUsersHandler(BaseHandler):

    def initialize(self, spider, injector, crawled_site):
        self.spider = spider
        self.injector = injector
        self.crawled_site = crawled_site

    def get(self):
        scrapydo.run_spider(self.spider,
                            crawl_reason='get-db-users',
                            injector=self.injector,
                            settings=DVWA_CRAWLER_SETTINGS)

        storage_adapter = FileAdapter()

        parser = GetDbUsersParser(self.crawled_site, storage_adapter)
        db_usernames = parser.get_db_usernames()

        self.write(json.dumps(db_usernames))

    def post(self):
        pass
