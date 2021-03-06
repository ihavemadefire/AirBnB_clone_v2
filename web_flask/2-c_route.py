#!/usr/bin/python3
"""Defines the routhing for a simple flask app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """This routes to the root page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB_ext():
    """This routes to another page"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def HBNB_text(text):
    """This accepts text as input and renders the result"""
    text1 = text.replace("_", " ")
    return ("C {}".format(text1))

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000)
