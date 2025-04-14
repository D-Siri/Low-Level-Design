from Coffee import Coffee


class EspressoCoffee(Coffee):

    def set_price(self, price=5):
        self.price = price

    def set_recipe(self, recipe):
        self.recipe = recipe
