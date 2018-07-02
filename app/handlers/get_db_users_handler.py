""" This module contains """
import json
from scrapy.crawler import CrawlerProcess
from app.handlers.base_handler import BaseHandler
from app.parsers.get_db_users import GetDbUsersParser
from constants import USER_AGENT_KEY, CRAWLER_PROCESS_USER_AGENT, ITEM_PIPELINES_KEY, \
    CRAWLER_PIPELINE


class GetDbUsersHandler(BaseHandler):
    """ This class is a tornado handler in charge of """

    def initialize(self, spider, injector, crawled_site):
        self.spider = spider
        self.injector = injector
        self.crawled_site = crawled_site

    def get(self):
        process = CrawlerProcess({
            USER_AGENT_KEY: CRAWLER_PROCESS_USER_AGENT,
            ITEM_PIPELINES_KEY: CRAWLER_PIPELINE
        })

        process.crawl(self.spider,
                      crawl_reason='get-db-users',
                      injector=self.injector)
        process.start()

        parser = GetDbUsersParser(self.crawled_site)
        db_usernames = parser.get_db_usernames()

        self.write(json.dumps(db_usernames))

    def post(self):
        pass
