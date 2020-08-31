#!/usr/bin/python3
"""DOCSTRING"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    strict_slashes = False
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB_ext():
    strict_slashes = False
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def HBNB_text(text):
    text1 = text.replace("_", " ")
    return ("C {}".format(text1))

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000)
