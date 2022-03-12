from .normal_item import NormalItem


class ConjuredItem(NormalItem):
    def update_quality(self):
        if self.get_sell_in() > 0:
            self.modify_quality(-2)
        else:
            self.modify_quality(-4)
        self.set_sell_in()
