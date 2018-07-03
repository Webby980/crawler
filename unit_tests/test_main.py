from mock import patch
import unittest
from crawler.spiders.dvwa_spider import DVWASpider

from main import make_app
from app.handlers.check_vulnerability_handler import CheckVulnerabilityHandler
from app.handlers.get_db_version_handler import GetDbVersionHandler
from app.handlers.get_db_users_handler import GetDbUsersHandler


class TestMain(unittest.TestCase):

    @patch('main.Sql')
    @patch('main.tornado.web.Application')
    def test__main__make_app__WillInitialiseTornadoApplicationWithCorrectHandlers__WhenCalled(self, mock_app, mock_sql):

        mock_sql_instance = mock_sql.return_value

        expected_args = [('/check-vulnerability', CheckVulnerabilityHandler, dict(spider=DVWASpider, injector=mock_sql_instance, crawled_site='dvwa')),
                         ('/get-db-users', GetDbUsersHandler, dict(spider=DVWASpider, injector=mock_sql_instance, crawled_site='dvwa')),
                         ('/get-db-version', GetDbVersionHandler, dict(spider=DVWASpider, injector=mock_sql_instance, crawled_site='dvwa'))]

        make_app()

        mock_app.assert_called_with(expected_args)