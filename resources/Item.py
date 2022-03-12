from resources.ItemResource import ItemResource
from services import Services


class Item(ItemResource):
    def get(self, item):
        return Services.get_item(item)
