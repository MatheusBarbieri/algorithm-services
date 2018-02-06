from tests.routes import RouteTestCase
from algorithm_services.app import get_index_data


class IndexRouteTestCase(RouteTestCase):

    def setUp(self):
        super(IndexRouteTestCase, self).setUp()
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

    def test_get_index_data_not_found(self):
        test_string = 'abcdefgh'
        self.assertEqual(get_index_data(test_string), '')
