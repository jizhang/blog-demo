from marshmallow import Schema, fields, validate

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class PostSchema(Schema):
    id = fields.Int()
    title = fields.Str(required=True, validate=validate.Length(min=1))
    content = fields.Str(required=True, validate=validate.Length(min=1))
    updated_at = fields.DateTime(format=DATETIME_FORMAT)


post_schema = PostSchema()
