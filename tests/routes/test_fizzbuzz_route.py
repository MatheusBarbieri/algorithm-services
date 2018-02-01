import unittest

from algorithm_services.app import create_app
from algorithm_services.config import config


class FizzBuzzRouteTestCase(unittest.TestCase):

    def setUp(self):
        _app = create_app(__name__, config)
        self.app = _app.test_client()

    def test_fizzbuzz(self):
        result = self.app.get('/fizzbuzz/15')

        self.assertEqual(
            b'[1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]',  # noqa
            result.data
        )

    def test_fizzbuzz_response(self):
        result = self.app.get('fizzbuzz/1')

        self.assertEqual('application/json', result.content_type)
        self.assertEqual('200 OK', result.status)

    def test_fizzbuzz_argument_validation(self):
        result = self.app.get('fizzbuzz/five')

        self.assertEqual('404 NOT FOUND', result.status)
        self.assertEqual('text/html', result.content_type)
        self.assertTrue(
            b'The requested URL was not found on the server.'
            in result.data
        )
