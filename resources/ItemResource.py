from functools import wraps
from flask_restful import Resource
from domain import AgedBrie, Backstage, ConjuredItem, NormalItem, Sulfuras, Items


def request_to_item(func):
    @wraps(func)
    def create_item(*args, **kwargs):
        name = kwargs["name"]
        sell_in = int(kwargs["sell_in"]) if kwargs.get("sell_in") else None
        quality = int(kwargs["quality"]) if kwargs.get("quality") else None

        if name == Items.AgedBrie:
            item = AgedBrie(name, sell_in, quality)

        elif name == Items.Backstage:
            item = Backstage(name, sell_in, quality)

        elif name == Items.ConjuredItem:
            item = ConjuredItem(name, sell_in, quality)

        elif name == Items.Sulfuras:
            item = Sulfuras(name, sell_in, quality)

        else:
            item = NormalItem(name, sell_in, quality)

        return func(item)

    return create_item


class ItemResource(Resource):
    method_decorators = [request_to_item]
