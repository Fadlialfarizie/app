from marshmallow import Schema, fields, validate, EXCLUDE


class ProductSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Int(dump_only=True)
    produk = fields.Str(required=True)
    harga = fields.Float(required=True,validate=validate.Range(min=0))
    stok = fields.Int(required=True,validate=validate.Range(min=0))