from tests.routes import RouteTestCase


class FizzbuzzRouteTestCase(RouteTestCase):

    def test_fizzbuzz(self):
        result = self.app.get('/fizzbuzz/15')

        self.assertEqual(
            b'[1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]',  # noqa
            result.data
        )

    def test_fizzbuzz_response(self):
        self.algorithm_json_response(self.app, 'fizzbuzz/1')

    def test_fizzbuzz_argument_validation(self):
        self.algorithm_argument_validation(self.app, 'fizzbuzz/five')
