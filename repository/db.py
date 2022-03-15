from .connection import get_db


class DB:
    @staticmethod
    def get_all():
        db = get_db()
        return db.find({}, {"_id": False})

    @staticmethod
    def get_one(item):
        db = get_db()
        return db.find_one(item.__dict__, {"_id": False})

    @staticmethod
    def filter_item(item):
        db = get_db()
        return db.find(
            {k: v for k, v in item.__dict__.items() if v is not None}, {"_id": False}
        )

    @staticmethod
    def create_one(item):
        db = get_db()
        db.insert_one({k: v if v is not None else 0 for k, v in item.__dict__.items()})

    @staticmethod
    def update_one(item):
        db = get_db()
        db.update_one({"name": item.get_name()}, {"$set": item.__dict__})

    @staticmethod
    def delete_one(item):
        db = get_db()
        db.delete_one({k: v for k, v in item.__dict__.items() if v is not None})
