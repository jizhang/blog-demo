from typing import Optional, Dict
from threading import Lock

from flask import Flask, current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session


class Holder:
    sessions: Dict[str, scoped_session]
    lock: Lock

    def __init__(self):
        self.sessions = {}
        self.lock = Lock()


class SQLAlchemyMulti:
    def __init__(self, app: Optional[Flask] = None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        app.extensions['sqlalchemy_multi'] = Holder()
        app.teardown_appcontext(self.teardown)

    def connect(self, name: str) -> scoped_session:
        if name == 'default':
            url = current_app.config['SQLALCHEMY_DATABASE_URI']
        else:
            url = current_app.config['SQLALCHEMY_BINDS'][name]

        echo = current_app.config.get('SQLALCHEMY_ECHO', False)

        engine = create_engine(url, echo=echo)
        session_factory = sessionmaker(bind=engine)
        return scoped_session(session_factory)

    def teardown(self, exception) -> None:
        holder: Holder = current_app.extensions['sqlalchemy_multi']
        for session in holder.sessions.values():
            session.remove()

    def get_session(self, name: str = 'default') -> Session:
        holder: Holder = current_app.extensions['sqlalchemy_multi']
        with holder.lock:
            if name not in holder.sessions:
                holder.sessions[name] = self.connect(name)
            return holder.sessions[name]()
