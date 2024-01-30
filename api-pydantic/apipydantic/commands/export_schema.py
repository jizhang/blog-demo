import json

from pydantic.json_schema import models_json_schema

from apipydantic import app
from apipydantic.views.user import CreateUserResponse, UserForm


@app.cli.command()
def export_schema() -> None:
    _, schema = models_json_schema([
        (UserForm, 'validation'),
        (CreateUserResponse, 'serialization'),
    ])
    with open('schemas.json', 'w') as f:
        f.write(json.dumps(schema, indent=2))
