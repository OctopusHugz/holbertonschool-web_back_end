#!/usr/bin/env python3
""" End-to-end integration test of User Authentication Service """
from flask import jsonify
import requests


def register_user(email: str, password: str) -> None:
    """ Testing register_user function """
    data = {"email": email, "password": password}
    response = requests.post("http://localhost:5000/users", data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """ Testing log_in_wrong_password function """
    data = {"email": email, "password": password}
    response = requests.post("http://0.0.0.0:5000/sessions", data)
    # assert


def log_in(email: str, password: str) -> str:
    """ Testing log_in function """
    data = {"email": email, "password": password}
    response = requests.post("http://0.0.0.0:5000/sessions", data)
    # assert


def profile_unlogged() -> None:
    """ Testing profile_unlogged function """
    response = requests.get("http://0.0.0.0:5000/profile")
    # assert


def profile_logged(session_id: str) -> None:
    """ Testing profile_logged function """
    data = {"session_id": session_id}
    response = requests.get("http://0.0.0.0:5000/profile", data)
    # assert


def log_out(session_id: str) -> None:
    """ Testing log_out function """
    data = {"session_id": session_id}
    response = requests.delete("http://0.0.0.0:5000/sessions", data)
    # assert


def reset_password_token(email: str) -> str:
    """ Testing reset_password_token function """
    data = {"email": email}
    response = requests.post("http://0.0.0.0:5000/reset_password", data)
    # assert


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Testing update_password function """
    data = {"email": email, "reset_token": reset_token,
            "new_password": new_password}
    response = requests.put("http://0.0.0.0:5000/reset_password", data)
    # assert


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    # log_in_wrong_password(EMAIL, NEW_PASSWD)
    # profile_unlogged()
    # session_id = log_in(EMAIL, PASSWD)
    # profile_logged(session_id)
    # log_out(session_id)
    # reset_token = reset_password_token(EMAIL)
    # update_password(EMAIL, reset_token, NEW_PASSWD)
    # log_in(EMAIL, NEW_PASSWD)
