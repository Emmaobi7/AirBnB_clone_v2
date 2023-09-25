#!/usr/bin/python3
"""A minial flask app"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    function to greet
    at root/
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display text
    at /hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """
    passing args
    at //
    """
    if ('_' in text):
        new = text.replace('_', " ")
        return f"C {escape(new)}"
    else:
        return f"C {escape(text)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
