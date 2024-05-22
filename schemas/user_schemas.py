from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    name = fields.Str(required=False)
    tk = fields.Str(required=False)
    created_at = fields.DateTime()