#!/usr/bin/python3
"""Defines the routhing for a simple flask app"""

from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def listofstates():
    """This renders a list of states"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)
