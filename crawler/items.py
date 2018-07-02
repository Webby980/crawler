import scrapy


class CrawlerItem(scrapy.Item):
    url = scrapy.Field()
    body = scrapy.Field()
    crawl_reason = scrapy.Field()
