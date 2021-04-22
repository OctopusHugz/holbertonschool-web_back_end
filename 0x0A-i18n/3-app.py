#!/usr/bin/env python3
""" This module creates a Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from typing import Text
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class for babel """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index() -> Text:
    """ Returns the index.html page """
    return render_template("3-index.html", home_title=gettext(u"home_title"),
                           home_header=gettext(u"home_header"))


@babel.localeselector
def get_locale() -> str:
    """ Gets the locale from request.accept_languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])
