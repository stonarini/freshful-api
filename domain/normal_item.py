from .updateable import Updateable
from .item import Item


class NormalItem(Item, Updateable):
    def get_name(self):
        return self.name

    def get_sell_in(self):
        return self.sell_in

    def set_sell_in(self):
        self.sell_in -= 1

    def get_quality(self):
        return self.quality

    def set_quality(self, quality):
        self.quality = quality

    def modify_quality(self, modifier):
        if self.get_quality() + modifier >= 50:
            self.set_quality(50)
        elif self.get_quality() + modifier <= 0:
            self.set_quality(0)
        else:
            self.set_quality(self.get_quality() + modifier)

    def update_quality(self):
        if self.get_sell_in() > 0:
            self.modify_quality(-1)
        else:
            self.modify_quality(-2)
        self.set_sell_in()

    def __len__(self):
        return len(list(filter(lambda a: a[1], self.__dict__.items())))