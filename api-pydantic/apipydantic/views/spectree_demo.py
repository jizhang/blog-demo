from pydantic.v1 import BaseModel, Field
from spectree import Response

from apipydantic import app, spec
from apipydantic.models.user import User as UserOrm


class UserForm(BaseModel):
    username: str = Field(min_length=3, max_length=10)
    password: str = Field(exclude=True)


class CreateUserResponse(BaseModel):
    id: int


@app.post('/spectree/create-user')
@spec.validate(resp=Response(HTTP_200=CreateUserResponse))
def spectree_create_user(json: UserForm) -> CreateUserResponse:
    user_orm = UserOrm(username=json.username, password=json.username)
    return CreateUserResponse(id=user_orm.id)
