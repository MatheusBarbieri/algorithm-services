import unittest


from algorithm_services.algorithms.algorithm_runner import AlgorithmRunner
from algorithm_services.algorithms.clock_angle import ClockAngle


class AlgorithmRunnerTestCase(unittest.TestCase):
    def setUp(self):
        self.test_algorithm = ClockAngle('clock_angle', [15, 45])

    def test_algorithm_runner_miss(self):
        runner = AlgorithmRunner({})
        self.assertEqual(runner.execute(self.test_algorithm), 157.5)

    def test_algorithm_runner_hit(self):
        key = ('clock_angle', tuple([15, 45]))
        runner = AlgorithmRunner({key: 157.5})
        self.assertEqual(runner.execute(self.test_algorithm), 157.5)
