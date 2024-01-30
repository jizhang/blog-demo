import json
from datetime import datetime
from enum import IntEnum
from pprint import pprint
from typing import Annotated, Any

from flask import abort, request
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PlainSerializer,
    TypeAdapter,
    computed_field,
    validate_call,
)
from pydantic.alias_generators import to_camel
from pydantic.json_schema import models_json_schema

from apipydantic import app, db
from apipydantic.models.user import User as UserOrm
from apipydantic.services import user as user_svc


def format_datetime(dt: datetime):
    return dt.strftime('%Y-%m-%d %H:%M:%S')


CustomDatetime = Annotated[datetime, PlainSerializer(format_datetime)]


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int # = Field(serialization_alias='user_id')
    username: str
    last_login: datetime

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
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    user_list: list[User]
    # total_count: int = Field(ge=0)

    # @model_serializer
    # def serialize_model(self) -> list:
    #     return self.users

class UserDto:
    def __init__(self, id: int, username: str, last_login: datetime):
        self.id = id
        self.username = username
        self.last_login = last_login


@app.get('/current-user')
def current_user() -> dict:
    pprint(UserListResponse.model_json_schema())

    # user = User(id=1, username='jizhang', last_login=datetime.now())
    # user = User.model_validate({'id': 1, 'username': 'jizhang', 'last_login': datetime.now()})
    # user = User.model_validate(UserDto(1, 'jizhang', datetime.now()))
    user = User.model_validate(UserDto(1, 'jizhang', datetime.now()), from_attributes=True)
    user.context['test'] = 'abc'
    user.model_dump_json()
    return user.model_dump(mode='json', by_alias=True)


@app.get('/get-user')
def get_user() -> dict:
    user_orm = user_svc.get_user(int(request.args['id']))
    if user_orm is None:
        abort(404)
    response = User.model_validate(user_orm)
    return response.model_dump(mode='json')


@app.get('/user-list')
def user_list() -> dict:
    user_orms = user_svc.get_list()
    # response = UserListResponse(users=user_orms, total_count=len(user_orms))
    response = UserListResponse.model_validate({'user_list': user_orms})
    return response.model_dump(mode='json', by_alias=True)


@app.get('/user-list-raw')
def user_list_raw() -> list:
    user_orms = user_svc.get_list()
    UserList = TypeAdapter(list[User])  # noqa: N806
    user_list = UserList.validate_python(user_orms)
    return UserList.dump_python(user_list, mode='json')


class LoginForm(BaseModel):
    username: str
    password: str
    remember_me: bool = True


@app.post('/login')
def login() -> dict:
    form = LoginForm.model_validate(request.get_json())
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



def validate_name(value: str) -> str:
    if len(value) < 3 or len(value) > 10:
        raise ValueError('should have 3 to 10 characters')
    return value


class UserForm(BaseModel):
    username: str = Field(min_length=3, max_length=10)
    password: str = Field(exclude=True)

    # @field_validator('username')
    # @classmethod
    # def validate_username(cls, value: str) -> str:
    #     if len(value) < 3 or len(value) > 10:
    #         # raise ValueError('should have 3 to 10 characters')
    #         raise PydanticCustomError('bad_request', 'Invalid username', {'code': 40001})
    #     return value

    # @model_validator(mode='after')
    # def validate_model(self) -> 'UserForm':
    #     if len(self.username) < 3 or len(self.username) > 10:
    #         raise ValueError('username should have 3 to 10 characters')
    #     return self


class CreateUserResponse(BaseModel):
    id: int


@app.post('/create-user')
def create_user() -> dict:
    _, schema = models_json_schema([
        (UserForm, 'validation'),
        (CreateUserResponse, 'serialization'),
    ])
    print(json.dumps(schema, indent=2))

    pprint(request.get_json())
    form = UserForm.model_validate(request.get_json())
    user_orm = UserOrm(**dict(form), last_login=datetime.now())
    db.session.add(user_orm)
    db.session.commit()

    response = CreateUserResponse(id=user_orm.id)
    return response.model_dump(mode='json')
