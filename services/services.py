from repository import DB


class Services:
    @staticmethod
    def get_items():
        return list(DB.get_all())

    @staticmethod
    def get_item(item):
        if len(item) < 3:
            return list(DB.filter_item(item))
        else:
            return DB.get_one(item)

    @staticmethod
    def create_item(item):
        DB.create_one(item)

    @staticmethod
    def update_item(item):
        return list(DB.update_one(item))

    @staticmethod
    def delete_item(item):
        return list(DB.delete_one(item))
