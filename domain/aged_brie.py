from .normal_item import NormalItem


class AgedBrie(NormalItem):
    def update_quality(self):
        if self.get_sell_in() > 0:
            self.modify_quality(1)
        else:
            self.modify_quality(2)
        self.set_sell_in()
