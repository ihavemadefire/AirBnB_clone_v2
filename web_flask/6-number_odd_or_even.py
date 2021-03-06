#!/usr/bin/python3
"""Defines the routhing for a simple flask app"""

from flask import Flask
from flask import render_template
app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """This routes to the root page"""
    strict_slashes = False
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB_ext():
    """This routes to another page"""
    strict_slashes = False
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def HBNB_text(text):
    """This accepts text as input and renders the result"""
    text1 = text.replace("_", " ")
    return ("C {}".format(text1))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def HBNB_text_python(text="is cool"):
    """This routes to a file, but set a default value"""
    text1 = text.replace("_", " ")
    return ("Python {}".format(text1))


@app.route('/number/<int:n>', strict_slashes=False)
def HBNB_is_int(n):
    """This accepts an int as input and renders the result if int"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def HBNB_is_int_template(n):
    """This accepts an int as input and renders html if int"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def HBNB_odd_even(n):
    """This accepts an int as input and renders html for even|odd"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)
