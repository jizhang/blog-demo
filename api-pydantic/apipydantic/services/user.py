from collections.abc import Sequence
from typing import Optional

from sqlalchemy import select

from apipydantic import db
from apipydantic.models.user import User


def get_user(id: int) -> Optional[User]:
    return db.session.get(User, id)


def get_list() -> Sequence[User]:
    return db.session.scalars(select(User)).all()
