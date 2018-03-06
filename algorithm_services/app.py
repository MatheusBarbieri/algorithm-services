import json
import markdown
import re
import os.path

from flask import Flask
from flask import Response
from flask import render_template
from flask import Markup

from algorithm_services.algorithms.algorithm_factory import AlgorithmFactory
from algorithm_services.algorithms.algorithm_runner import AlgorithmRunner


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
    app = Flask(name, template_folder=config['TEMPLATE_FOLDER'])
    app.config.update(config)
    app.algorithm_runner = AlgorithmRunner({})

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

    @app.route('/<string:algorithm_name>/<path:args>')
    def algorithm_route(algorithm_name, args):
        args = args.split('/')
        algorithm = AlgorithmFactory.create_algorithm(algorithm_name, args)
        result = app.algorithm_runner.execute(algorithm)

        result_json = json.dumps(result)
        return Response(
            response=result_json,
            status=200,
            mimetype='application/json'
        )

    return app
