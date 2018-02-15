import unittest


from algorithm_services.algorithms.algorithm_factory import AlgorithmFactory


class AlgorithmFactoryTestCase(unittest.TestCase):

    def test_algorithm_factory(self):
        fizzbuzz = AlgorithmFactory.create_algorithm('fizzbuzz', [3])
        self.assertEqual(fizzbuzz.run(), [1, 2, 'Fizz'])
        self.assertEqual(fizzbuzz.name, "fizzbuzz")

    def test_name_to_class_name(self):
        class_name = AlgorithmFactory._name_to_class_name('clock_angle')
        self.assertEqual(class_name, 'ClockAngle')
