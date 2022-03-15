from functools import wraps
from typing import OrderedDict
from flask import request
from flask_restful import Resource, abort
from .schema import ItemSchema
from domain import AgedBrie, Backstage, ConjuredItem, NormalItem, Sulfuras, Items


def request_to_item(func):
    @wraps(func)
    def create_item(*args, **kwargs):
        schema = ItemSchema()
        errors = schema.validate(request.args)
        if errors:
            abort(400)

        item_args = OrderedDict({"name": None, "sell_in": None, "quality": None})
        item_args.update(**schema.dump(request.args))

        name = request.args["name"]
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

        return func(item)

    return create_item


class ItemResource(Resource):
    method_decorators = [request_to_item]
