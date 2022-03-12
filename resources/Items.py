from flask_restful import Resource
from services import Services


class Items(Resource):
    def get(self):
        return Services.get_items()
