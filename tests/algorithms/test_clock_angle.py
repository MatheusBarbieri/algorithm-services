import unittest

from algorithm_services.algorithms.clock_angle import ClockAngle


class ClockAngleTestCase(unittest.TestCase):
    def setUp(self):
        self.teste_instance_0 = ClockAngle("clock_angle", [12, 0])
        self.teste_instance_1 = ClockAngle("clock_angle", [15, 30])
        self.teste_instance_2 = ClockAngle("clock_angle", [15, 45, 30])
        self.teste_instance_3 = ClockAngle("clock_angle", [12, 45])
        self.teste_instance_4 = ClockAngle("clock_angle", [17, 37])
        self.teste_instance_5 = ClockAngle("clock_angle", [12, 45, 0])
        self.teste_instance_6 = ClockAngle("clock_angle", [5, 37])

    def test_clock_angle(self):
        self.assertEqual(self.teste_instance_0.run(), 0)
        self.assertEqual(self.teste_instance_1.run(), 75)
        self.assertEqual(self.teste_instance_2.run(), 160.25)
        self.assertEqual(self.teste_instance_3.run(), self.teste_instance_5.run()) # noqa
        self.assertEqual(self.teste_instance_4.run(), self.teste_instance_6.run()) # noqa
