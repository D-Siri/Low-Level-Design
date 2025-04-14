from abc import ABC, abstractmethod


class Coffee(ABC):

    def __init__(self):
        self.price = 0
        self.recipe = None

    @abstractmethod
    def set_price(self, price):
        self.price = price

    @abstractmethod
    def set_recipe(self, recipe):
        self.recipe = recipe

    def get_price(self):
        return self.price

