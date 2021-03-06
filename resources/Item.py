from resources.ItemResource import ItemResource
from services import Services


class Item(ItemResource):
    def get(self, item):
        return Services.get_item(item)

    def put(self, item):
        return Services.create_item(item)

    def patch(self, item):
        return Services.update_item(item)

    def delete(self, item):
        return Services.delete_item(item)
