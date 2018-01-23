import unittest

from algorithm_services.algorithms.clock_angle import clock_angle


class ClockAngleTestCase(unittest.TestCase):

    def test_clock_angle(self):
        self.assertEqual(clock_angle(12, 0), 0)
        self.assertEqual(clock_angle(15, 30), 75)
        self.assertEqual(clock_angle(15, 45, 30), 160.25)
        self.assertEqual(clock_angle(12, 45), clock_angle(12, 45, 0))
        self.assertEqual(clock_angle(17, 37), clock_angle(5, 37))
