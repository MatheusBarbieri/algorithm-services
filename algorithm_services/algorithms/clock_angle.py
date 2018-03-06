from algorithm_services.algorithms import Algorithm


class ClockAngle(Algorithm):
    name = "clock_angle"

    hour_displacement_per_hour = 30
    hour_displacement_per_minute = 0.5
    hour_displacement_per_second = 0.5/60
    minute_displacement_per_minute = 6
    minute_displacement_per_second = 0.1

    def function(self, hours, minutes, seconds=0):
        hours, minutes, seconds = int(hours), int(minutes), int(seconds)
        hour_angle = (
            (hours % 12) * self.hour_displacement_per_hour +
            minutes * self.hour_displacement_per_minute +
            seconds * self.hour_displacement_per_second
        )
        minutes_angle = (
            minutes * self.minute_displacement_per_minute +
            seconds * self.minute_displacement_per_second
        )
        angle = abs(hour_angle - minutes_angle)
        return angle if angle <= 180 else 360 - angle
