from datetime import datetime
from typing import Optional

from flask import Response, jsonify, request
from sqlmodel import Field, SQLModel

from apipydantic import app, db


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    last_login: datetime


@app.get('/sqlmodel/current-user')
def sqlmodel_current_user() -> dict:
    user = db.session.get_one(User, 1)
    return user.model_dump(mode='json')


@app.post('/sqlmodel/create-user')
def sqlmodel_create_user() -> Response:
    user = User.model_validate(request.get_json())
    db.session.add(user)
    db.session.commit()
    return jsonify(id=user.id)
