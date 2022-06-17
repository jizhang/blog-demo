from typing import Optional

from marshmallow import Schema, fields, validate, validates, ValidationError

from oasis import db
from oasis.models import Post

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class PostSchema(Schema):
    id = fields.Integer()
    title = fields.String(required=True, validate=validate.Length(min=1))
    content = fields.String(required=True, validate=validate.Length(min=1))
    updated_at = fields.DateTime(format=DATETIME_FORMAT, dump_only=True)

    @validates('id')
    def validate_id(self, value: Optional[int]):
        if not value:
            return

        post = db.session.query(Post).get(value)
        if post is None:
            raise ValidationError('Post ID not found.')


post_schema = PostSchema()
