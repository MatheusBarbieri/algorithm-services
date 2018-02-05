from algorithm_services.algorithms import Algorithm


class ClockAngle(Algorithm):

    def function(self, hours, minutes, seconds=0):
        hours, minutes, seconds = int(hours), int(minutes), int(seconds)
        hour_angle = (hours % 12) * 30 + minutes * 0.5 + seconds * 0.5/60
        minutes_angle = minutes * 6 + seconds * 0.1
        angle = abs(hour_angle - minutes_angle)
        return angle if angle <= 180 else 360 - angle
