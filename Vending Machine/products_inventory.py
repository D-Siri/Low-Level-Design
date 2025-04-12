from collections import defaultdict


class ProductsInventory:
    def __init__(self):
        self.products = defaultdict(int)

    def add_product(self, product):
        self.products[product] += 1

    def __getitem__(self, product_id):
        return self.products.get(product_id)

