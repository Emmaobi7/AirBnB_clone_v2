#!/usr/bin/python3
"""a basic flask app"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cities_of_state(id=None):
    """list cities of a state
    """
    states = storage.all('State')
    if id:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def clean_up(exception):
    """remove alchemy session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
