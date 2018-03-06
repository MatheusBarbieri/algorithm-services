from flask import abort


class Algorithm():
    name = "undefined"

    def __init__(self, args):
        self.args = args

    def run(self):
        '''
            Catchs cases where the user inputs less arguments
            or arguments with wrong type
        '''
        try:
            result = self.function(*self.args)
        except TypeError:
            return abort(404)
        except ValueError:
            return abort(404)
        return result

    def function(self, args):
        pass
