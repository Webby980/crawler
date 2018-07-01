from scrapy.crawler import CrawlerProcess
from crawler.spiders.dvwa_spider import DVWASpider
from crawler.injectors.sql import Sql
from constants import USER_AGENT_KEY, CRAWLER_PROCESS_USER_AGENT

if __name__ == "__main__":
    process = CrawlerProcess({
        USER_AGENT_KEY: CRAWLER_PROCESS_USER_AGENT
    })

    injector = Sql()
    spider = DVWASpider()

    process.crawl(spider)
    process.start()
