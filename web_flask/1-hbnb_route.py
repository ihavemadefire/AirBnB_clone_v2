#!/usr/bin/python3
# Launches simple flask app

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB_ext():
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)