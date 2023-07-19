# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify

app = Flask(__name__)


class BadRequest(Exception):
    """Custom exception class to be thrown when local error occurs."""
    def __init__(self, message, status=400, payload=None):
        self.message = message
        self.status = status
        self.payload = payload


@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Catch BadRequest exception globally, serialize into JSON, and respond with 400."""
    payload = dict(error.payload or ())
    payload['status'] = error.status
    payload['message'] = error.message
    return jsonify(payload), 400


@app.route('/person', methods=['POST'])
def person_post():
    """Create a new person object and return its ID"""
    if not request.form.get('username'):
        raise BadRequest('username cannot be empty', 40001, { 'ext': 1 })
    return jsonify(last_insert_id=1)


@app.route('/ping')
def ping():
    return jsonify('pong')


@app.route('/login', methods=['POST'])
def login():
    form = request.get_json()
    if form['username'] == 'admin' and form['password'] == '888888':
        return jsonify(1)
    raise BadRequest('invalid username or password', 40001)
