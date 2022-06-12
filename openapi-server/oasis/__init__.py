from typing import Any

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('timetable.default_settings')

db: Any = SQLAlchemy(app)


class AppError(Exception):
    status_code = 400


# pylint: disable=cyclic-import,wrong-import-position
import oasis.views.api
import oasis.commands.gen
