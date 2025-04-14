from collections import defaultdict


class CoffeeRecipe:
    def __init__(self):
        self.items = defaultdict(int)

    def add_ingredients(self, item, quantity):
        self.items[item] += quantity
