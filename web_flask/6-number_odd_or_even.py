#!/usr/bin/python3
"""A minial flask app"""

from flask import Flask, render_template
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
    new = text.replace('_', " ")
    return f"C {escape(new)}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_is(text='is cool'):
    """
    python_is: displa Python...
    text: text to display
    """
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    """
    is_num: checks for int
    n: user input
    """
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n=None):
    """
    num_template: render template
    if type (int)
    Args:
        n: number
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n=None):
    """
    odd_even: checks for number
    Args:
        n: int number
    """
    if n % 2 == 0:
        var = 'even'
    else:
        var = 'odd'
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
