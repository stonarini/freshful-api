from flask_restful import Resource
from services import Services


class Book(Resource):
    def get(self, title):
        return Services.get_item(title)
