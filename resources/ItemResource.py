from functools import wraps
from flask import request
from flask_restful import Resource, abort
from .schema import ItemSchema
from repository.db import get_db


def request_to_item(func):
    @wraps(func)
    def validate_route(*args, **kwargs):
        schema = ItemSchema()
        name = kwargs["name"]

        raw_item = {"name": name, **request.args}

        if schema.validate(raw_item):
            abort(400)

        item = schema.load(schema.dump(raw_item))
        get_db("GildedRose")
        return func(item)

    return validate_route


class ItemResource(Resource):
    method_decorators = [request_to_item]
