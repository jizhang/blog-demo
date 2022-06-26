from typing import Optional

from flask import Flask, current_app
from flask.globals import _app_ctx_stack, _app_ctx_err_msg
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


class SQLAlchemyAlpha:
    def __init__(self, app: Optional[Flask] = None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'sqlite://')
        app.teardown_appcontext(self.teardown)

    def connect(self) -> Engine:
        return create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])

    def teardown(self, exception) -> None:
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'sqlalchemy'):
            ctx.sqlalchemy.dispose()

    @property
    def engine(self) -> Engine:
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'sqlalchemy'):
                ctx.sqlalchemy = self.connect()
            return ctx.sqlalchemy
        raise RuntimeError(_app_ctx_err_msg)
