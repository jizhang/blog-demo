import click
from flask import Flask
from flask.cli import FlaskGroup
from flask_sqlalchemy import SQLAlchemy

from . import default_settings
from .utils import load_module_recursively

db = SQLAlchemy()


def create_app(web: bool = True) -> Flask:
    app = Flask(__name__)
    app.config.from_object(default_settings)
    app.config.from_envvar('APP_CONFIG', silent=True)

    db.init_app(app)

    if web:
        configure_views(app)

    else:
        configure_jobs(app)

    return app


def configure_views(app: Flask):
    with app.app_context():
        # pylint: disable=import-outside-toplevel
        from modern import views
        load_module_recursively(views)


def configure_jobs(app: Flask):
    with app.app_context():
        # pylint: disable=import-outside-toplevel
        from modern import jobs
        load_module_recursively(jobs)


@click.group(cls=FlaskGroup, create_app=lambda: create_app(web=False), add_default_commands=False)
def cli():
    """Management script for the Modern application."""
