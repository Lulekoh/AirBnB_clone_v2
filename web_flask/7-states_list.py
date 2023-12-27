#!/usr/bin/python3
"""script that runs a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontent
def teardown_appcontext(exception):
    """method that handles storage.close()"""
    storage.close()


@app.route('/states_lsit', strict_slashes=False)
def states():
    """list all states"""
    states = storage.all('State')
    return render_template(
            '7-states_list.html',
            table='States',
            states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
