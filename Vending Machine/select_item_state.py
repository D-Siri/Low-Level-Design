from vending_machine_state import VendingMachineState
from dispense_state import DispenseState

class SelectItemState(VendingMachineState):

    def insert_money(self, money):
        print(f"Cannot insert money while selecting product items")

    def select_product(self, product):
        if self.vending_machine.inventory[product] > 0:
            self.vending_machine.selected_product = product
            print(f"Selected {product.id}")
            self.vending_machine.set_state(self.vending_machine.dispense_state)
            self.vending_machine.dispense_product()
        else:
            print(f"Sorry, selected product is unavailable!, choose a different a product")

    def dispense_product(self):
        print("Select a product to dispense!")

    def return_change(self):
        print("cannot return change while selecting products")
