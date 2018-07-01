import scrapy
from loginform import fill_login_form
from constants import DVWA_PAGES
from config import DVWA_BASE_URL, DVWA_PASSWORD, DVWA_USER_NAME


class DVWASpider(scrapy.Spider):

    def __init__(self):
        super().__init__()

    name = "dvwa"

    def start_requests(self):
        yield scrapy.Request(DVWA_BASE_URL + 'login.php', self.parse_login)

    def parse_login(self, response):
        data, url, method = fill_login_form(response.url,
                                            response.body,
                                            DVWA_USER_NAME,
                                            DVWA_PASSWORD)
        return scrapy.FormRequest(url,
                                  formdata=dict(data),
                                  method=method,
                                  callback=self.after_login)

    def after_login(self, _response):
        for page in DVWA_PAGES:
            yield scrapy.Request(url=DVWA_BASE_URL + page, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'dvwa-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
