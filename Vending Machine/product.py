class Product:
    def __init__(self, price, product_id):
        self.price = price
        self.id = product_id

    def get_price(self):
        return self.price
