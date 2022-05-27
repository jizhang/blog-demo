import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from . import default_settings
from .utils import import_submodules

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(default_settings)
    app.config.from_envvar('APP_CONFIG', silent=True)

    configure_logging(app)
    configure_db(app)
    configure_views(app)

    return app


def configure_logging(app: Flask):
    logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s')
    logging.getLogger().setLevel(logging.INFO)

    if app.debug:
        logging.getLogger().setLevel(logging.DEBUG)

        # Make sure engine.echo is set to False
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

        # Fix werkzeug handler in debug mode
        logging.getLogger('werkzeug').handlers = []


def configure_db(app: Flask):
    db.init_app(app)


def configure_views(app: Flask):
    with app.app_context():
        # pylint: disable=import-outside-toplevel
        from . import views, jobs
        import_submodules(views)
        import_submodules(jobs)
