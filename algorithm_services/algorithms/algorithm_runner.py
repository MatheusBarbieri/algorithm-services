class AlgorithmRunner():

    def __init__(self, cache_dict={}):
        self.cache = cache_dict

    def execute(self, algorithm):
        hashable_args = tuple(algorithm.args)
        key = (algorithm.name, hashable_args)

        if key in self.cache:
            result = self.cache[key]
        else:
            result = algorithm.run()
            self.cache[key] = result

        return result
