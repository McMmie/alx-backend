#!/usr/bin/env python3
"""
This is a basic flask app
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """
    a basic method that returns HTML
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
