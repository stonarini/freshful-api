from functools import wraps
from flask_restful import Resource


def request_to_item(func):
    @wraps(func)
    def create_item(*args, **kwargs):
        print(args)
        print(kwargs)

    return create_item


class ItemResource(Resource):
    method_decorators = [request_to_item]
