#!/usr/bin/python3
""" setting up babel """
from flask import Flask
from flask_babel import Babel


app = Flask(__name__)

class Config:
    """ has a language class attribute to set languages and do translations"""
    LANGUAGES = ["en", "fr", "es"]

app.config['BABEL_DEFAULT_LOCALE'] = 'Config.LANGUAGES[0]'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
