#!/usr/bin/env python3
""" This module creates a Flask app """
from auth import Auth
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
