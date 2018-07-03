import scrapydo
from app.handlers.base_handler import BaseHandler
from app.storage.file_adapter import FileAdapter
from app.parsers.get_db_version import GetDbVersionParser
from config import DVWA_CRAWLER_SETTINGS

scrapydo.setup()


class GetDbVersionHandler(BaseHandler):

    def initialize(self, spider, injector, crawled_site):
        self.spider = spider
        self.injector = injector
        self.crawled_site = crawled_site

    def get(self):
        scrapydo.run_spider(self.spider,
                            crawl_reason='get-db-version',
                            injector=self.injector,
                            settings=DVWA_CRAWLER_SETTINGS)

        storage_adapter = FileAdapter()

        parser = GetDbVersionParser(self.crawled_site, storage_adapter)
        db_version = parser.get_db_version()

        self.write({'db_version': db_version})

    def post(self):
        pass
