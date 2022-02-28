from flask_restful import Resource
from model.db import DB


class Book(Resource):
    def get(self, title):
        return DB.get_item(title)
