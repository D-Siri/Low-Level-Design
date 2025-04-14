from collections import defaultdict

class ProductsInventory:
    def __init__(self):
        self.coffee_inventory = defaultdict(int)

    def add_product(self, coffee):
        self.coffee_inventory[coffee] += 1

    def __getitem__(self, coffee):
        return self.coffee_inventory.get(coffee)

    def is_available(self, coffee):
        if self.coffee_inventory[coffee] > 0:
            return True
        else:
            return False

    def select_product(self, coffee):
        self.coffee_inventory[coffee] -= 1
        if self.coffee_inventory[coffee] < 1:
            print(f"{coffee} outof stock \n")

    def show_products(self):
        print(self.coffee_inventory.items())

