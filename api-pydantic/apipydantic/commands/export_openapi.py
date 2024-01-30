from openapi_pydantic import OpenAPI
from openapi_pydantic.util import PydanticSchema, construct_open_api_with_schema_class

from apipydantic import app
from apipydantic.views.user import CreateUserResponse, UserForm


@app.cli.command()
def export_openapi() -> None:
    api = OpenAPI.model_validate({
        'info': {'title': 'Pydantic Demo', 'version': '0.1.0'},
        'paths': {
            '/create-user': {
                'post': {
                    'requestBody': {'content': {'application/json': {
                        'schema': PydanticSchema(schema_class=UserForm),
                    }}},
                    'responses': {'200': {
                        'description': 'OK',
                        'content': {'application/json': {
                            'schema': PydanticSchema(schema_class=CreateUserResponse),
                        }},
                    }},
                },
            },
        },
    })
    api = construct_open_api_with_schema_class(api)
    print(api.model_dump_json(by_alias=True, exclude_none=True, indent=2))
