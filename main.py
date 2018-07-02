import tornado.ioloop
import tornado.web
from crawler.spiders.dvwa_spider import DVWASpider
from crawler.injectors.sql import Sql
from app.handlers.check_vulnerability_handler import CheckVulnerabilityHandler
from app.handlers.get_db_users_handler import GetDbUsersHandler
from app.handlers.get_db_version_handler import GetDbVersionHandler
from constants import FORM_ID_KEY, SQL_SYNTAX_ERROR_PAYLOAD, DVWA_SITE_NAME, \
    SQL_GET_DB_USER_PAYLOAD, SQL_GET_DB_VERSION_PAYLOAD


def make_app():
    check_vulnerability_injector = Sql(FORM_ID_KEY, SQL_SYNTAX_ERROR_PAYLOAD)
    get_db_user_injector = Sql(FORM_ID_KEY, SQL_GET_DB_USER_PAYLOAD)
    get_db_version_injector = Sql(FORM_ID_KEY, SQL_GET_DB_VERSION_PAYLOAD)

    return tornado.web.Application([
        (r'/check-vulnerability', CheckVulnerabilityHandler,
         dict(spider=DVWASpider,
              injector=check_vulnerability_injector,
              crawled_site=DVWA_SITE_NAME)
         ),
        (r'/get-db-users', GetDbUsersHandler,
         dict(spider=DVWASpider,
              injector=get_db_user_injector,
              crawled_site=DVWA_SITE_NAME)
         ),
        (r'/get-db-version', GetDbVersionHandler,
         dict(spider=DVWASpider,
              injector=get_db_version_injector,
              crawled_site=DVWA_SITE_NAME)
         )
    ])


if __name__ == "__main__":
    """ This function is the entry point for the application. """
    app = make_app()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()
