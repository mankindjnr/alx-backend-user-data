#!/usr/bin/env python3
"""
basic falsk app
"""
from flask import Flask, abort, jsonify, request, make_response, redirect
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
def session():
    """function responds to the sessions route"""
    data = request.form
    email = data.get('email')
    passwd = data.get('password')

    if not AUTH.valid_login(email, passwd):
        abort(401)

    new_session = AUTH.create_session(email)

    resp_data = {
        "email": email,
        "message": "logged in"
        }
    response = jsonify(resp_data)
    response = make_response(response)
    response.set_cookie("session_id", new_session)

    return response


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
