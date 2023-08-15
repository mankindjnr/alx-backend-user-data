#!/usr/bin/env python3
"""
basic falsk app
"""
from flask import Flask, abort, jsonify, request, make_response
from flask import url_for, redirect, session
from auth import Auth
import flask


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def payload():
    """returning a jsonified string"""
    return flask.jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users():
    """handle the user route data"""
    try:
        data = request.form
        email = data.get('email')
        passwd = data.get('password')

        user = AUTH.register_user(email, passwd)
        response = {"email": user.email, "message": "user created"}
        return jsonify(response), 200
    except ValueError as e:
        response = {"message": "email already registered"}
        return jsonify(response), 400


@app.route("/sessions", methods=['POST'])
def login():
    """function responds to the login sessions route"""
    data = request.form
    email = data.get('email')
    passwd = data.get('password')

    if not AUTH.valid_login(email, passwd):
        abort(401)

    session_id = AUTH.create_session(email)

    response = make_response(jsonify({
        "email": email,
        "message": "logged in"}))
    response.set_cookie("session_id", session_id)

    return response


@app.route("/profile", methods=["GET"])
def profile():
    """a profile function"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route("reset_password", methods=["POST"])
def get_reset_password_token():
    """the reset password token"""
    data = request.form
    email = data.get('email')

    user = AUTH.get_user(email)
    if user is None:
        abort(403)

    token = AUTH.get_reset_password_token(email)
    return jsonify({
        "email": user.email,
        "reset_token": token
    })


@app.route("/reset_password", methods=["PUT"])
def update_password():
    """updating the users password"""
    data = request.form
    email = data.get('email')
    reset_token = data.get('reset_token')
    new_password = data.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)

    return jsonify({
        "email": user.email,
        "message": "Password updated"
    }), 200


@app.route("/sessions", methods=['DELETE'])
def logout():
    """logout function"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user or user is None:
        abort(403)

    if user:
        session.clear()
        return redirect(url_for("payload"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
