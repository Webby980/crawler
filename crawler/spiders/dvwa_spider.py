import scrapy
from loginform import fill_login_form
from crawler.injectors.sql import Sql
from crawler.items import CrawlerItem
from constants import DVWA_VULNERABILITY_ENDPOINTS, DVWA_LOGIN_ENDPOINT
from config import DVWA_BASE_URL, DVWA_PASSWORD, DVWA_USER_NAME


class DVWASpider(scrapy.Spider):

    def __init__(self):
        super().__init__('dvwa')
        self.injector = Sql()

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
        page = response.url.split("/")[-2]
        filename = 'dvwa-%s.html' % page
        with open(filename, 'wb') as file:
            file.write(response.body)
        self.log('Saved file %s' % filename)
