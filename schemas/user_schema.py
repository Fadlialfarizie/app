from marshmallow import Schema, fields,validate, EXCLUDE


class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE


    username = fields.Str(required=True, validate=validate.Length(min=3))
    password= fields.Str(load_only=True, validate=validate.Length(min=8))