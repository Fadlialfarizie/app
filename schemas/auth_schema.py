from marshmallow import Schema, fields, EXCLUDE, validate


class RegisterSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=15))
    password = fields.Str(required=True, validate=validate.Length(min=8))
    role = fields.Str(required=True)


class LoginSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    username = fields.Str(required=True, validate=validate.Length(min=3, max=15))
    password = fields.Str(required=True, validate=validate.Length(min=8))