import importlib


class AlgorithmFactory():

    @classmethod
    def create_algorithm(cls, name, args):
        module = importlib.import_module(
            'algorithm_services.algorithms.' + name
        )

        attr = cls._name_to_class_name(name)
        Algorithm = getattr(module, attr)

        return Algorithm(args)

    @classmethod
    def _name_to_class_name(cls, name):
        out = ""
        words = name.split('_')
        for word in words:
            out += word[0].upper() + word[1:]
        return out
