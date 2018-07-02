""" This module contains """
import scrapydo
from app.handlers.base_handler import BaseHandler
from app.parsers.get_db_version import GetDbVersionParser
from constants import USER_AGENT_KEY, CRAWLER_PROCESS_USER_AGENT, ITEM_PIPELINES_KEY, \
    CRAWLER_PIPELINE

scrapydo.setup()


class GetDbVersionHandler(BaseHandler):
    """ This class is a tornado handler in charge of """

    def initialize(self, spider, injector, crawled_site):
        self.spider = spider
        self.injector = injector
        self.crawled_site = crawled_site

    def get(self):

        scrapydo.run_spider(self.spider, crawl_reason='get-db-version', injector=self.injector,
                            settings={
                                USER_AGENT_KEY: CRAWLER_PROCESS_USER_AGENT,
                                ITEM_PIPELINES_KEY: CRAWLER_PIPELINE
                            })

        parser = GetDbVersionParser(self.crawled_site)
        db_version = parser.get_db_version()

        self.write({'db_version': db_version})

    def post(self):
        pass
