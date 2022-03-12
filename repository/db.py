from .connection import get_db


class DB:
    @staticmethod
    def get_all():
        db = get_db()
        return db.find({}, {"_id": False})

    @staticmethod
    def get_one(item):
        db = get_db()
        return db.find_one(
            {
                "name": item.get_name(),
                "sell_in": item.get_sell_in(),
                "quality": item.get_quality(),
            },
            {"_id": False},
        )

    @staticmethod
    def get_by_name(name):
        db = get_db()
        return db.find(
            {"name": name},
            {"_id": False},
        )

    @staticmethod
    def create_one(item):
        db = get_db()
        db.insert_one(
            {
                "name": item.get_name(),
                "sell_in": item.get_sell_in(),
                "quality": item.get_quality(),
            }
        )

    @staticmethod
    def update_one():
        pass

    @staticmethod
    def delete_one():
        pass
