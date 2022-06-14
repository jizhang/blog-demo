from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

from oasis import app, views, schemas

spec = APISpec(
    title='Oasis',
    version='0.1.0',
    openapi_version='3.0.2',
    info={'description': 'Demo project for OpenAPI workflow.'},
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)

spec.components.schema('Post', schema=schemas.PostSchema)

with app.test_request_context():
    spec.path(view=views.get_post_list)
