from .normal_item import NormalItem


class Backstage(NormalItem):
    def update_quality(self):
        if self.get_sell_in() > 10:
            self.modify_quality(1)
        elif self.get_sell_in() > 5:
            self.modify_quality(2)
        elif self.get_sell_in() > 0:
            self.modify_quality(3)
        else:
            self.set_quality(0)
        self.set_sell_in()
