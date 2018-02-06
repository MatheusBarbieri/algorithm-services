from tests.routes import RouteTestCase


class ClockAngleRouteTestCase(RouteTestCase):

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
        self.algorithm_json_response(self.app, 'clock_angle/0/0')

    def test_clock_angle_argument_validation(self):
        self.algorithm_argument_validation(self.app, 'clock_angle/15')
