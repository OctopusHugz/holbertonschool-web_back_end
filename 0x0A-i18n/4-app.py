#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    return render_template("4-index.html", home_title=gettext(u"home_title"),
                           home_header=gettext(u"home_header"))


@babel.localeselector
def get_locale():
    locale = request.args.get("locale")
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])
