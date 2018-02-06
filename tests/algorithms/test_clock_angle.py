import unittest

from algorithm_services.algorithms.clock_angle import ClockAngle


class ClockAngleTestCase(unittest.TestCase):
    def setUp(self):
        self.teste_instance_0 = ClockAngle([12, 0]) # noqa
        self.teste_instance_1 = ClockAngle([15, 30]) # noqa
        self.teste_instance_2 = ClockAngle([15, 45, 30]) # noqa
        self.teste_instance_3 = ClockAngle([12, 45]) # noqa
        self.teste_instance_4 = ClockAngle([17, 37]) # noqa
        self.teste_instance_5 = ClockAngle([12, 45, 0]) # noqa
        self.teste_instance_6 = ClockAngle([5, 37]) # noqa

    def test_clock_angle(self):
        self.assertEqual(self.teste_instance_0.run(), 0)
        self.assertEqual(self.teste_instance_1.run(), 75)
        self.assertEqual(self.teste_instance_2.run(), 160.25)
        self.assertEqual(self.teste_instance_3.run(), self.teste_instance_5.run()) # noqa
        self.assertEqual(self.teste_instance_4.run(), self.teste_instance_6.run()) # noqa
