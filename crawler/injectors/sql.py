import scrapy
from constants import SECURITY_COOKIE_KEY, SECURITY_COOKIE_LOW_VALUE


class Sql:

    def __init__(self, attribute_id, payload):
        self.attribute_id = attribute_id
        self.payload = payload

    def post_data(self, response):
        form_data = {
            self.attribute_id: self.payload
        }
        return scrapy.FormRequest.from_response(response,
                                                cookies={
                                                    SECURITY_COOKIE_KEY: SECURITY_COOKIE_LOW_VALUE
                                                },
                                                formid=self.attribute_id,
                                                formdata=form_data)