from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Home'


@app.route('/algorithm/<algorithm>')
def run_algorithm(algorithm):
    return str(algorithm)
