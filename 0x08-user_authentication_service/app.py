#!/usr/bin/env python3
""" This module creates a Flask app """
from auth import Auth
from flask import abort, Flask, jsonify, redirect, request
from flask.helpers import make_response
from sqlalchemy.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=["GET"])
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
            AUTH.destroy_session(found_user.id)
            # redirect to GET /
            # do I need to add 302 code?
            return redirect("/")
    # If the user does not exist, respond with a 403 HTTP status.
    return abort(403)


# Do I need to add GET to methods here?
@app.route('/profile')
def profile():
    """ Returns a users profile if it exists """
    session_id = request.cookies.get("session_id")
    if session_id is not None:
        # Use it to find the user.
        found_user = AUTH.get_user_from_session_id(session_id)
        if found_user is not None:
            # If the user exist, respond with a 200 HTTP status and
            # the following JSON payload {"email": "<user email>"}
            return jsonify({"email": found_user.email})
    # If the session ID is invalid or the user does not exist,
    # respond with a 403 HTTP status
    return abort(403)


@app.route('/reset_password', methods=["POST"])
def get_reset_password_token():
    """ Returns jsonified reset password token if user exists """
    email = request.form.get("email")
    try:
        AUTH._db.find_user_by(email=email)
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token})
    except NoResultFound:
        abort(403)


@app.route('/reset_password', methods=["PUT"])
def update_password():
    """ Updates a user's password and returns JSONified response """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        AUTH._db.find_user_by(email=email)
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"})
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
