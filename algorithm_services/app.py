import json
import markdown
import re
import os.path
import jinja2

from flask import Flask
from flask import render_template
from flask import Response
from flask import Markup

from algorithm_services.algorithms.fizzbuzz import fizzbuzz
from algorithm_services.algorithms.clock_angle import clock_angle


def get_readme_algorithms_doc(readme_data):
    found = re.search(
        '### Available algorithms(.+?)### Tests',
        readme_data,
        re.DOTALL
    )
    if found:
        algorithms_data = """### Basic usage
        - Syntax: <server domain>/<algorithm (lower case)>/<inputs>
        - Example: localhost:8888/fizzbuzz/20
        """
        algorithms_data += '\n### Available Algorithms\n'
        algorithms_data += found.group(1)
    return algorithms_data


def create_app(name, config):
    app = Flask(name)
    app.config.update(config)

    app_loader = jinja2.FileSystemLoader(
                os.path.abspath('./algorithm_services/templates') # noqa
    )

    app.jinja_loader = app_loader

    @app.route('/')
    def index():
        with open(os.path.abspath('README.md')) as file:
            readme_data = file.read()

        algorithms_data = get_readme_algorithms_doc(readme_data)
        algorithms = Markup(markdown.markdown(algorithms_data, extensions=['markdown.extensions.tables'])) # noqa

        return render_template('index.html', **locals())

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
