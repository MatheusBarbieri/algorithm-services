import unittest

from algorithm_services.algorithms.fizzbuzz import Fizzbuzz


class FizzBuzzTestCase(unittest.TestCase):

    def setUp(self):

        self.result = Fizzbuzz([15]).run()

    def test_fizz(self):
        self.assertEqual(self.result[2], 'Fizz')
        self.assertEqual(self.result[8], 'Fizz')
        self.assertNotEqual(self.result[12], 'Fizz')

    def test_buzz(self):
        self.assertEqual(self.result[4], 'Buzz')
        self.assertEqual(self.result[9], 'Buzz')
        self.assertNotEqual(self.result[10], 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(self.result[14], 'FizzBuzz')
        self.assertNotEqual(self.result[9], 'FizzBuzz')

    def test_number(self):
        self.assertEqual(self.result[6], 7)
        self.assertEqual(self.result[1], 2)
        self.assertEqual(self.result[0], 1)

    def test_fizzbuzz_sequence(self):
        self.assertEqual(self.result, [
            1, 2, 'Fizz', 4, 'Buzz', 'Fizz',
            7, 8, 'Fizz', 'Buzz', 11,
            'Fizz', 13, 14, 'FizzBuzz'
        ])
