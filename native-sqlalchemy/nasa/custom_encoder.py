from json import JSONEncoder
from decimal import Decimal
from datetime import datetime

from sqlalchemy.engine.row import Row
from sqlalchemy.orm.decl_api import DeclarativeMeta


class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)

        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        if isinstance(obj, Row):
            return dict(obj)

        if isinstance(obj.__class__, DeclarativeMeta):
            return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

        return super().default(obj)
