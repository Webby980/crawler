import scrapy
from loginform import fill_login_form
from crawler.items import CrawlerItem

from constants import DVWA_VULNERABILITY_ENDPOINTS, DVWA_LOGIN_ENDPOINT, \
    DVWA_CRAWLER_NAME
from config import DVWA_BASE_URL, DVWA_PASSWORD, DVWA_USER_NAME


class DVWASpider(scrapy.Spider):

    name = DVWA_CRAWLER_NAME

    def __init__(self, crawl_reason, injector):
        super().__init__()
        self.crawl_reason = crawl_reason
        self.injector = injector

    def start_requests(self):
        yield scrapy.Request(DVWA_BASE_URL + DVWA_LOGIN_ENDPOINT,
                             callback=self.login)

    def login(self, response):
        data, url, method = fill_login_form(response.url,
                                            response.body,
                                            DVWA_USER_NAME,
                                            DVWA_PASSWORD)
        yield scrapy.FormRequest(url,
                                 formdata=dict(data),
                                 method=method,
                                 callback=self.post_login)

    def post_login(self, _response):
        for endpoint in DVWA_VULNERABILITY_ENDPOINTS:
            yield scrapy.Request(url=DVWA_BASE_URL + endpoint,
                                 callback=self.process_page)

    def process_page(self, response):
        yield self.injector.post_data(response)

    def parse(self, response):
        item = CrawlerItem()
        item['crawl_reason'] = self.crawl_reason
        item['url'] = response.url
        item['body'] = response.body
        yield item
