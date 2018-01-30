import json

from flask import Flask
from flask import render_template
from flask import Response

from algorithm_services.algorithms.fizzbuzz import fizzbuzz
from algorithm_services.algorithms.clock_angle import clock_angle


def create_app(name, config):
    app = Flask(name)
    app.config.update(config)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/fizzbuzz/<int:number>')
    def fizzbuzz_route(number):
        result = json.dumps(fizzbuzz(number))
        return Response(
            response=result,
            status=200,
            mimetype='application/json'
        )

    @app.route('/clock_angle/<int:hours>/<int:minutes>')
    @app.route('/clock_angle/<int:hours>/<int:minutes>/<int:seconds>')
    def clock_angle_route(hours, minutes, seconds=0):
        result = json.dumps(clock_angle(hours, minutes, seconds))
        return Response(
            response=result,
            status=200,
            mimetype='application/json'
        )

    return app
