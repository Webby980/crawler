""" This is the main module for the application. It is in charge of creating and configuring the
tornado web server app. """
import tornado.ioloop
import tornado.web
from crawler.spiders.dvwa_spider import DVWASpider
from crawler.injectors.sql import Sql
from app.handlers.check_vulnerability_handler import CheckVulnerabilityHandler
from app.handlers.exploit_vulnerability_handler import ExploitVulnerabilityHandler
from constants import FORM_ID_KEY, SQL_SYNTAX_ERROR_PAYLOAD, DVWA_SITE_NAME, \
    SQL_GET_DB_USER_PAYLOAD


def make_app():
    """ This function returns an Application instance which holds the request
        handlers for the app. """
    check_vulnerability_injector = Sql(FORM_ID_KEY, SQL_SYNTAX_ERROR_PAYLOAD)
    exploit_vulnerability_injector = Sql(FORM_ID_KEY, SQL_GET_DB_USER_PAYLOAD)

    return tornado.web.Application([
        (r'/check-vulnerability', CheckVulnerabilityHandler,
         dict(spider=DVWASpider,
              injector=check_vulnerability_injector,
              crawled_site=DVWA_SITE_NAME)
         ),
        (r'/exploit-vulnerability', ExploitVulnerabilityHandler,
         dict(spider=DVWASpider,
              injector=exploit_vulnerability_injector,
              crawled_site=DVWA_SITE_NAME)
         )
    ])


if __name__ == "__main__":
    """ This function is the entry point for the application. """
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
