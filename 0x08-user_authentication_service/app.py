#!/usr/bin/env python3
""" This module creates a Flask app """
from flask.helpers import make_response
from auth import Auth
from flask import abort, Flask, jsonify, redirect, request
app = Flask(__name__)
AUTH = Auth()


@app.route('/')
# Do I really need to add methods=["GET"] in decorator?
def hello():
    """ Returns a jsonified message """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"])
def users():
    """ Implements the POST /users route """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        new_user = AUTH.register_user(email, password)
        if new_user is not None:
            return jsonify({"email": email,
                            "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=["POST"])
def login():
    """ Login a user to a session """
    email = request.form.get("email")
    password = request.form.get("password")
    valid_user = AUTH.valid_login(email, password)
    if valid_user:
        session_id = AUTH.create_session(email)
        if session_id is not None:
            response = make_response(
                jsonify({"email": email, "message": "logged in"}))
            response.set_cookie("session_id", session_id)
            return response
    else:
        abort(401)


@app.route('/sessions', methods=["DELETE"])
def logout():
    """ Logs a user out of a session """
    # The request is expected to contain the session ID
    # as a cookie with key "session_id"
    session_id = request.cookies.get("session_id")
    if session_id is not None:
        # Find the user with the requested session ID.
        found_user = AUTH.get_user_from_session_id(session_id)
        if found_user is not None:
            # If the user exists destroy the session
            AUTH.destroy_session(found_user.user_id)
            # redirect to GET /
            # do I need to add 302 code?
            return redirect("/")

        else:
            # If the user does not exist, respond with a 403 HTTP status.
            return jsonify({}, 403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
