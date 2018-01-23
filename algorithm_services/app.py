import json

from flask import Flask
from flask import render_template
from flask import Response

from algorithm_services.algorithms.fizzbuzz import fizzbuzz


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

    return app
