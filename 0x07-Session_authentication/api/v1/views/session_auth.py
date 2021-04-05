#!/usr/bin/env python3
""" Module of SessionAuth views
"""
from flask.helpers import make_response
from api.v1.views import app_views
from flask import jsonify, request, session
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """ POST /api/v1/auth_session/login
    Return:
      - User object JSON represented
      - 400 if email or password is missing/empty
      - 401 if password is incorrect
      - 404 if no User is found for the provided email
    """
    from api.v1.app import auth
    user_email = request.form.get("email")
    user_password = request.form.get("password")
    if user_email is None or user_email == "":
        return jsonify({"error": "email missing"}), 400
    elif user_password is None or user_password == "":
        return jsonify({"error": "password missing"}), 400
    user_list = User.search({"email": user_email})
    if len(user_list) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    user = user_list[0]
    if not user.is_valid_password(user_password):
        return jsonify({"error": "wrong password"}), 401
    session_id = auth.create_session(user.id)
    cookie_name = os.getenv("SESSION_NAME")
    response = make_response(user.to_json())
    response.set_cookie(cookie_name, session_id)
    return response
