from typing import Optional

from flask import Flask, current_app
from flask.globals import _app_ctx_stack, _app_ctx_err_msg
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class SQLAlchemy:
    def __init__(self, app: Optional[Flask] = None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        url = app.config['SQLALCHEMY_DATABASE_URI']
        app.logger.info(f'Create engine {url}')

        echo = app.config.get('SQLALCHEMY_ECHO', False)
        app.extensions['sqlalchemy'] = create_engine(url, echo=echo)

        app.teardown_appcontext(self.teardown)

    def connect(self) -> Session:
        return Session(current_app.extensions['sqlalchemy'])

    def teardown(self, exception) -> None:
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'sqlalchemy_session'):
            ctx.sqlalchemy_session.close()

    @property
    def session(self) -> Session:
        ctx = _app_ctx_stack.top
        if ctx is None:
            raise RuntimeError(_app_ctx_err_msg)
        if not hasattr(ctx, 'sqlalchemy_session'):
            ctx.sqlalchemy_session = self.connect()
        return ctx.sqlalchemy_session
