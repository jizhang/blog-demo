from marshmallow import Schema, fields, validate

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class PostSchema(Schema):
    id = fields.Integer()
    title = fields.String(required=True, validate=validate.Length(min=1))
    content = fields.String(required=True, validate=validate.Length(min=1))
    updated_at = fields.DateTime(format=DATETIME_FORMAT)


post_schema = PostSchema()
