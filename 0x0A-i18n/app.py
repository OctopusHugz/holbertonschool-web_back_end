#!/usr/bin/env python3
from flask import Flask, g, render_template, request
from flask_babel import Babel, gettext
from pytz import UnknownTimeZoneError, timezone
app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    if g.user_id in users.keys():
        logged_in = True
    else:
        logged_in = False
    logged_in_as = gettext(u"logged_in_as", username=None)
    if logged_in:
        logged_in_as = gettext(
            u"logged_in_as", username=g.user.get("name"))
    return render_template("index.html", logged_in=logged_in,
                           logged_in_as=logged_in_as, home_title=gettext(
                               u"home_title"),
                           home_header=gettext(u"home_header"),
                           not_logged_in=gettext(u"not_logged_in"))


@babel.localeselector
def get_locale():
    url_locale = request.args.get("locale")
    if url_locale is not None and url_locale in Config.LANGUAGES:
        return url_locale
    if g.user is not None:
        user_locale = g.user.get("locale")
        if user_locale is not None and user_locale in Config.LANGUAGES:
            return user_locale
    header_locale = request.headers.get("Accept-Language")
    if header_locale is not None and header_locale in Config.LANGUAGES:
        return header_locale
    return Config.BABEL_DEFAULT_LOCALE


def get_user(user_id):
    return users.get(user_id)


@app.before_request
def before_request():
    user_id = request.args.get("login_as")
    if user_id is not None:
        user_id = int(user_id)
    g.user_id = user_id
    g.user = get_user(user_id)
    g.locale = get_locale()
    g.timezone = get_timezone()


@babel.timezoneselector
def get_timezone():
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
