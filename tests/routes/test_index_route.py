import unittest

from algorithm_services.app import create_app
from algorithm_services.app import get_index_data
from algorithm_services.config import config


class IndexRouteTestCase(unittest.TestCase):

    def setUp(self):
        _app = create_app(__name__, config)
        self.app = _app.test_client()
        self.index = self.app.get('/')

    def test_index_route(self):
        self.assertTrue('text/html' in self.index.content_type)
        self.assertEqual('200 OK', self.index.status)
        self.assertTrue(
            b'This is a webapp that permits the execution of algorithms'
            in self.index.data
        )

    def test_get_index_data(self):
        test_string = '### Available algorithmsABCD### Tests'
        self.assertEqual(get_index_data(test_string), 'ABCD')
