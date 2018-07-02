""" This module contains """
import json
import scrapydo
from app.handlers.base_handler import BaseHandler
from app.parsers.get_db_users import GetDbUsersParser
from constants import USER_AGENT_KEY, CRAWLER_PROCESS_USER_AGENT, ITEM_PIPELINES_KEY, \
    CRAWLER_PIPELINE

scrapydo.setup()


class GetDbUsersHandler(BaseHandler):
    """ This class is a tornado handler in charge of """

    def initialize(self, spider, injector, crawled_site):
        self.spider = spider
        self.injector = injector
        self.crawled_site = crawled_site

    def get(self):

        scrapydo.run_spider(self.spider, crawl_reason='get-db-users', injector=self.injector, settings={
            USER_AGENT_KEY: CRAWLER_PROCESS_USER_AGENT,
            ITEM_PIPELINES_KEY: CRAWLER_PIPELINE
        })

        parser = GetDbUsersParser(self.crawled_site)
        db_usernames = parser.get_db_usernames()

        self.write(json.dumps(db_usernames))

    def post(self):
        pass
