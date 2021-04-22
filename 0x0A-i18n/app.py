#!/usr/bin/env python3
""" This module creates a Flask app """
from datetime import datetime
from flask import Flask, g, render_template, request
from flask_babel import Babel, format_datetime, gettext
from pytz import UnknownTimeZoneError, timezone
import l18n
app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Config class for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """ Returns the index.html page """
    if g.user_id in users.keys():
        logged_in = True
    else:
        logged_in = False
    logged_in_as = gettext(u"logged_in_as", username=None)
    if logged_in:
        logged_in_as = gettext(
            u"logged_in_as", username=g.user.get("name"))
    now = format_datetime(datetime.now())
    return render_template("index.html", logged_in=logged_in,
                           logged_in_as=logged_in_as, home_title=gettext(
                               u"home_title"),
                           home_header=gettext(u"home_header"),
                           not_logged_in=gettext(u"not_logged_in"),
                           current_time_is=gettext(u"current_time_is",
                                                   current_time=now))


@babel.localeselector
def get_locale():
    """ Gets locale from query string, user settings, request.headers
    or returns the default from babel config """
    url_locale = request.args.get("locale")
    if url_locale is not None and url_locale in Config.LANGUAGES:
        return url_locale
    if g.user is not None:
        user_locale = g.user.get("locale")
        if user_locale is not None and user_locale in Config.LANGUAGES:
            return user_locale
    # if request.accept_languages is not None:
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    header_locale = request.headers.get("Accept-Language")
    if header_locale is not None and header_locale in Config.LANGUAGES:
        return header_locale
    return Config.BABEL_DEFAULT_LOCALE


def get_user(user_id):
    """ Returns the user based on user_id """
    return users.get(user_id)


@app.before_request
def before_request():
    """ Checks for login_as passed in query string and sets attributes """
    user_id = request.args.get("login_as")
    if user_id is not None:
        user_id = int(user_id)
    g.user_id = user_id
    g.user = get_user(user_id)
    g.locale = get_locale()
    g.timezone = get_timezone()


@babel.timezoneselector
def get_timezone():
    """ Gets timezone from query string, user settings, or returns default from
    babel config """
    url_timezone = request.args.get("timezone")
    if url_timezone is not None:
        try:
            timezone(url_timezone)
            return url_timezone
        except UnknownTimeZoneError:
            pass
    if g.user is not None:
        user_timezone = g.user.get("timezone")
        if user_timezone is not None:
            try:
                timezone(user_timezone)
                return user_timezone
            except UnknownTimeZoneError:
                pass
    return Config.BABEL_DEFAULT_TIMEZONE


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

# messages.mo isn't listed in files required, does that need to be original
# file from running babel stuff the first time in task 3?
