from algorithm_services.algorithms.fizzbuzz import Fizzbuzz
from algorithm_services.algorithms.clock_angle import ClockAngle


class AlgorithmFactory():

    @classmethod
    def create_algorithm(self, name, args):
        if name == 'fizzbuzz':
            return Fizzbuzz(args)
        if name == 'clock_angle':
            return ClockAngle(args)
