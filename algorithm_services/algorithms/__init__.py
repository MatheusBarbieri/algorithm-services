from flask import abort


class Algorithm():

    def __init__(self, name, args):
        self.name = name
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
