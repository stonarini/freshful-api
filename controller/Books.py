from flask_restful import Resource
from model.db import DB


class Books(Resource):
    def get(self):
        return DB.get_items()
