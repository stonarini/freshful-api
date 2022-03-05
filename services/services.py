from flask import g
from repository import get_db


class Services:
    @staticmethod
    def get_items():
        get_db()
        return list(g.db.find({}, {"_id": False}))

    @staticmethod
    def get_item(title):
        get_db()
        return list(g.db.find({"title": title}, {"_id": False}))
