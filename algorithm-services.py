import json
from flask import Flask, render_template, Response
from algorithm_services.config import config
from algorithm_services.algorithms.fizzbuzz import fizzbuzz

app = Flask(__name__)
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


app.run()
