import unittest

from algorithm_services.app import create_app
from algorithm_services.config import config


class RouteTestCase(unittest.TestCase):

    def setUp(self):
        _app = create_app(__name__, config)
        self.app = _app.test_client()


class RouteResponseTestCase(unittest.TestCase):

    def algorithm_json_response(self, result):
        self.assertEqual('application/json', result.content_type)
        self.assertEqual('200 OK', result.status)


class RouteArgumentValidationTestCase(unittest.TestCase):

    def algorithm_argument_validation(self, result):
        self.assertEqual('404 NOT FOUND', result.status)
        self.assertEqual('text/html', result.content_type)
        self.assertTrue(
            b'The requested URL was not found on the server.'
            in result.data
        )
