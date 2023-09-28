#!/usr/bin/python3

"""A basic web app"""


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filter():
    """
    load all cities of a state
    """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_request('10-hbnb_filters.html',
                          states=states, amenities=amenities)


@app.teardown_appcontext
def clean_up(exception):
    """
    remove alchemy session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
