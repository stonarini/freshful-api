from resources.ItemResource import ItemResource
from services import Services


class Book(ItemResource):
    def get(self, title):
        return Services.get_item(title)
