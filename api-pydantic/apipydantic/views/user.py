from dataclasses import dataclass
from datetime import datetime
from typing import Annotated

from flask import abort, request
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PlainSerializer,
    computed_field,
)

from apipydantic import app
from apipydantic.services import user as user_svc


def format_datetime(dt: datetime):
    return dt.strftime('%Y-%m-%d %H:%M:%S')


CustomDatetime = Annotated[datetime, PlainSerializer(format_datetime)]


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(serialization_alias='user_id')
    username: str
    last_login: CustomDatetime

    @computed_field  # type: ignore[misc]
    @property
    def last_login_timestamp(self) -> float:
        return self.last_login.timestamp()

    # @field_serializer('last_login')
    # def serialize_last_login(self, value: datetime):
    #     return value.strftime('%Y-%m-%d %H:%M:%S')

    # @model_serializer
    # def serialize_model(self) -> dict[str, Any]:
    #     return {
    #         'id': self.id,
    #         'username': self.username,
    #         'last_login': self.last_login.strftime('%Y-%m-%d %H:%M:%S'),
    #     }


class UserListResponse(BaseModel):
    users: list[User]
    total_count: int


@dataclass
class UserDTO:
    id: int
    username: str
    last_login: datetime


@app.get('/current-user')
def current_user() -> dict:
    # user = User(id=1, username='jizhang', last_login=datetime.now())
    user = User.model_validate({'id': 1, 'username': 'jizhang', 'last_login': datetime.now()})
    # user = User.model_validate(UserDTO(1, 'jizhang', datetime.now()))
    return user.model_dump(mode='json', by_alias=True)


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
