from flask import Flask, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from pydantic import ValidationError
from spectree import SpecTree

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../project.db'
db = SQLAlchemy(app)

spec = SpecTree('flask', annotations=True)
spec.register(app)


@app.errorhandler(ValidationError)
def handle_validation_error(error: ValidationError) -> tuple[Response, int]:
    detail = error.errors()[0]
    if detail['type'] == 'bad_request':
        payload = {
            'code': detail['ctx']['code'],
            'message': detail['msg'],
        }

    else:
        if detail['loc']:
            message = f'{detail["loc"][0]}: {detail["msg"]}'
        else:
            message = detail['msg']

        payload = {
            'code': 400,
            'message': message,
        }

    return jsonify(payload), 400


import apipydantic.commands
import apipydantic.views
