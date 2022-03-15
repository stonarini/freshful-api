from marshmallow import Schema, fields, post_load
from domain import AgedBrie, Backstage, ConjuredItem, Items, Sulfuras, NormalItem


class ItemSchema(Schema):
    name = fields.Str(required=True)
    sell_in = fields.Int(required=False, default=None, allow_none=True)
    quality = fields.Int(required=False, default=None, allow_none=True)

    @post_load
    def make_item(self, item_args, **kwargs):
        name = item_args["name"]
        if name == Items.AgedBrie:
            item = AgedBrie(**item_args)
        elif name == Items.Backstage:
            item = Backstage(**item_args)
        elif name == Items.ConjuredItem:
            item = ConjuredItem(**item_args)
        elif name == Items.Sulfuras:
            item = Sulfuras(**item_args)
        else:
            item = NormalItem(**item_args)
        return item
