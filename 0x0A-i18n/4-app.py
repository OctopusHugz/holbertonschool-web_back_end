#!/usr/bin/env python3
""" This module creates a Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """ Returns the index.html page """
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """ Gets the locale from query string or request.accept_languages """
    locale = request.args.get("locale")
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
