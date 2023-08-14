#!/usr/bin/env python3
"""
basic falsk app
"""
from flask import Flask, jsonify
import flask


app = Flask(__name__)


@app.route("/", methods=['GET'])
def payload():
    return flask.jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
