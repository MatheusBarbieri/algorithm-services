import json
import markdown
import re
import os.path

from flask import Flask
from flask import render_template
from flask import Response
from flask import Markup

from algorithm_services.algorithms.fizzbuzz import fizzbuzz
from algorithm_services.algorithms.clock_angle import clock_angle


def get_index_data(readme_data):
    found = re.search(
        '### Available algorithms(.+?)### Tests',
        readme_data,
        re.DOTALL
    )
    if found:
        return found.group(1)
    else:
        return ''


def create_app(name, config):
    template_folder = os.path.abspath(config['TEMPLATE_FOLDER'])
    app = Flask(name, template_folder=template_folder)
    app.config.update(config)

    @app.route('/')
    def index():
        with open(os.path.abspath('README.md')) as file:
            readme_data = file.read()

        index_data = get_index_data(readme_data)
        algorithms = Markup(
            markdown.markdown(
                index_data,
                extensions=['markdown.extensions.tables']
                )
        )

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
