from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from . import default_settings
from .utils import import_submodules

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(default_settings)
    app.config.from_envvar('APP_CONFIG', silent=True)

    db.init_app(app)

    with app.app_context():
        import_submodules('modern.views')
        import_submodules('modern.jobs')

    return app
