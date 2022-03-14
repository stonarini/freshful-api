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
        item_dict = dict(filter(lambda a: a[1], item.__dict__.items()))
        return db.find(item_dict, {"_id": False})

    @staticmethod
    def create_one(item):
        db = get_db()
        db.insert_one(item.__dict__)

    @staticmethod
    def update_one():
        pass

    @staticmethod
    def delete_one():
        pass
