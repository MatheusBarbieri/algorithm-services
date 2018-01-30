import unittest

from algorithm_services.app import create_app


class ClockAngleRouteTestCase(unittest.TestCase):

    def setUp(self):
        _app = create_app(__name__, {})
        self.app = _app.test_client()

    def test_clock_angle(self):
        result = self.app.get('/clock_angle/15/45')
        self.assertEqual(
            b'157.5',
            result.data
        )

        result_2 = self.app.get('/clock_angle/15/45/15')
        self.assertEqual(
            b'158.875',
            result_2.data
        )

    def test_clock_angle_response(self):
        result = self.app.get('clock_angle/0/0')

        self.assertEqual('application/json', result.content_type)
        self.assertEqual('200 OK', result.status)

    def test_clock_angle_argument_validation(self):
        result = self.app.get('clock_angle/15')

        self.assertEqual('404 NOT FOUND', result.status)
        self.assertEqual('text/html', result.content_type)
        self.assertTrue(
            b'The requested URL was not found on the server.'
            in result.data
        )
