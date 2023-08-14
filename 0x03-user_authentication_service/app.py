#!/usr/bin/env python3
"""
basic falsk app
"""
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
