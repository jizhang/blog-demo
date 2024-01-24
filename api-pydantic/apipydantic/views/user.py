from dataclasses import dataclass
from datetime import datetime
from typing import Annotated, Optional, Any
from enum import Enum, IntEnum

from flask import abort, request
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PlainSerializer, field_validator, validate_call,
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

    context: dict[str, Any] = Field(exclude=True, default={})

    @computed_field  # type: ignore[misc]
    @property
    def last_login_timestamp(self) -> float:
        return self.last_login.timestamp()

    @computed_field  # type: ignore[misc]
    @property
    def from_context(self) -> str:
        return self.context.get('test', 'N/A')

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
    user.context['test'] = 'abc'
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


class LoginForm(BaseModel):
    username: str
    password: str
    remember_me: bool = True


@app.post('/login')
def login() -> dict:
    form = LoginForm.model_validate(request.get_json())
    return form.model_dump(mode='json')


class FilterForm(BaseModel):
    tags: list[str] = []
    keyword: Optional[str] = None

    @field_validator('tags', mode='before')
    @classmethod
    def validate_tags(cls, value: str) -> list[str]:
        print(value)
        return [tag.strip() for tag in value.split(',') if tag.strip()]


@app.get('/filter')
def filter_by() -> dict:
    form = FilterForm.model_validate(request.args.to_dict())
    return form.model_dump(mode='json')


PositiveInt = Annotated[int, Field(gt=0)]

@app.get('/user/<int:user_id>')
@validate_call
def get_user_by_id(user_id: PositiveInt) -> dict:
    return {'id': user_id}


class Color(IntEnum):
    RED = 4
    GREEN = 5
    BLUE = 6


class ColorForm(BaseModel):
    color: Color


@app.post('/color')
def get_color() -> dict:
    form = ColorForm.model_validate(request.get_json())
    return form.model_dump(mode='json')
