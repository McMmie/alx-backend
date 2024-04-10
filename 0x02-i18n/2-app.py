#!/usr/bin/env python3
"""
using a babel decorator
"""
from flask import Flask, requests
from flask_babel import Babel


@babel.localeselector()
def get_locale():
    """
    using accept_languages  function to find the best match
    """
    return request.accept_languages.best_match(['en', 'fr'])

