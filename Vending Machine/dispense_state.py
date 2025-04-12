from vending_machine_state import VendingMachineState


class DispenseState(VendingMachineState):

    def insert_money(self, money):
        print(f"Cannot insert money while selecting products")

    def select_product(self, product_id):
        print(f"Cannot select a product now")

    def dispense_product(self):
        product = self.vending_machine.selected_product
        total_amount = self.vending_machine.get_amount()
        if total_amount >= product.get_price():
            count = self.vending_machine.get_product(product)
            count -= 1
            self.vending_machine.update_inventory(product, count)
            print(f"Dispensed {product.id}, Enjoy your snack!")
            total_amount -= product.get_price()
            self.vending_machine.set_amount(total_amount)
            self.vending_machine.selected_product = None
        else:
            print(f"Price of item is exceeding the current available amount, cannot complete the transaction.")
            self.vending_machine.set_state(self.vending_machine.return_change_state)

    def return_change(self):
        print(f"Cannot return change while selecting items!")
