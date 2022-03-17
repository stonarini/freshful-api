from flask import g
from .db import get_db


class DB:
    @staticmethod
    def get_all():
        get_db("GildedRose")
        return g.db.items.find({}, {"_id": False})

    @staticmethod
    def get_one(item):
        return g.db.items.find_one(item.__dict__, {"_id": False})

    @staticmethod
    def filter_item(item):
        return g.db.items.find(
            {k: v for k, v in item.__dict__.items() if v is not None}, {"_id": False}
        )

    @staticmethod
    def create_one(item):
        g.db.items.insert_one(
            {k: v if v is not None else 0 for k, v in item.__dict__.items()}
        )

    @staticmethod
    def update_one(item):
        g.db.items.update_one({"name": item.get_name()}, {"$set": item.__dict__})

    @staticmethod
    def delete_one(item):
        g.db.items.delete_one({k: v for k, v in item.__dict__.items() if v is not None})
