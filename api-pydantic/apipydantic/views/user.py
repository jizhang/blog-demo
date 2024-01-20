from datetime import datetime

from flask import abort, request
from pydantic import BaseModel, ConfigDict

from apipydantic import app
from apipydantic.services import user as user_svc


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    last_login: datetime


class UserListResponse(BaseModel):
    users: list[User]
    total_count: int


@app.get('/current-user')
def current_user() -> dict:
    user = User(id=1, username='jizhang', last_login=datetime.now())
    return user.model_dump(mode='json')


@app.get('/get-user')
def get_user() -> dict:
    user = user_svc.get_user(int(request.args['id']))
    if user is None:
        abort(404)
    response = User.model_validate(user)
    return response.model_dump(mode='json')


@app.get('/user-list')
def user_list() -> dict:
    users = user_svc.get_list()
    response = UserListResponse(users=users, total_count=len(users))
    return response.model_dump(mode='json')
