from typing import Any

from flask import Flask, Response, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('oasis.default_settings')

db: Any = SQLAlchemy(app)


class AppError(Exception):
    status_code = 400


@app.errorhandler(AppError)
def handle_app_error(error: AppError) -> Response:
    return make_response(str(error), error.status_code)


# pylint: disable=cyclic-import,wrong-import-position
import oasis.views
import oasis.commands
