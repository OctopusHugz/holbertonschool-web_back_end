#!/usr/bin/env python3
""" This module creates a Flask app """
from flask.helpers import make_response
from auth import Auth
from flask import abort, Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
