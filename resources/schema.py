from marshmallow import Schema, fields


class ItemSchema(Schema):
    name = fields.Str(required=True)
    sell_in = fields.Int(required=False)
    quality = fields.Int(required=False)
