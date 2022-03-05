from flask_restful import Resource
from services import Services


class Books(Resource):
    def get(self):
        return Services.get_items()
