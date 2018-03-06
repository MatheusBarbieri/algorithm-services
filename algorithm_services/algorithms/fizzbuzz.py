from algorithm_services.algorithms import Algorithm


class Fizzbuzz(Algorithm):
    name = "fizzbuzz"

    def function(self, input_number):
        input_number = int(input_number)
        output = []
        for number in range(1, input_number+1):
            out = ""
            if not number % 3:
                out += 'Fizz'
            if not number % 5:
                out += 'Buzz'
            if len(out) != 0:
                output.append(out)
            else:
                output.append(number)
        return output
