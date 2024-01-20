from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    last_login: Mapped[datetime]
