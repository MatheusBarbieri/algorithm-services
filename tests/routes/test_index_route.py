import unittest

from algorithm_services.app import create_app


class IndexRouteTestCase(unittest.TestCase):

    def setUp(self):
        _app = create_app(__name__, {})
        self.app = _app.test_client()
        self.index = self.app.get('/')

    def test_index_route(self):
        self.assertTrue('text/html' in self.index.content_type)
        self.assertEqual('200 OK', self.index.status)
        self.assertTrue(
            b'This is a webapp that permits the execution of algorithms'
            in self.index.data
        )
