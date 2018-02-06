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
        result = self.app.get('clock_angle/0/0')
        self.algorithm_json_response(result)

    def test_clock_angle_argument_validation(self):
        result = self.app.get('clock_angle/15')
        self.algorithm_argument_validation(result)
