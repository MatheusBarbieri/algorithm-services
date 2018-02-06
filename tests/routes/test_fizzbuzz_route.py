from tests.routes import RouteTestCase
from tests.routes import RouteResponseTestCase
from tests.routes import RouteArgumentValidationTestCase

class FizzbuzzRouteTestCase(RouteTestCase, RouteResponseTestCase, RouteArgumentValidationTestCase): # noqa

    def test_fizzbuzz(self):
        result = self.app.get('/fizzbuzz/15')

        self.assertEqual(
            b'[1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]',  # noqa
            result.data
        )

    def test_fizzbuzz_response(self):
        result = self.app.get('fizzbuzz/1')
        self.algorithm_json_response(result)

    def test_fizzbuzz_argument_validation(self):
        result = self.app.get('fizzbuzz/five')
        self.algorithm_argument_validation(result)
