from resources.ItemResource import ItemResource
from services import Services


class Item(ItemResource):
    def get(self, title):
        return Services.get_item(title)
