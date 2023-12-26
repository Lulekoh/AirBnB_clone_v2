#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask
import re


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def route_1():
    """first route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def route_2():
    """second route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def route_3(text):
    """third route"""
    new_text = re.sub(r"_", " ", text)
    return "C {}".format(new_text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def route_4(text='is cool'):
    """fourth route"""
    if text != 'is cool':
        text = re.sub(r"_", " ", text)
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def route_5(n):
    """fifth route"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def route_6(n):
    """sixth route"""
    return render_template("5-number.html", user=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def route_7(n):
    """seventh route"""
    return render_template("6-number_odd_or_even.html", num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
