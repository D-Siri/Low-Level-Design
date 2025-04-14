from coffee_vending_machine_state import CoffeeVendingMachineState
from ProductsInventory import ProductsInventory


class SelectCoffeeState(CoffeeVendingMachineState):

    def select_coffee(self, coffee):
        if self.vending_machine.inventory.is_available(coffee):
            print(f"Selected Coffee \n")
            return True
        return False

    def make_payment(self, money):
        print(f"Select an item to make payment! \n")

    def dispense_coffee(self):
        print(f"Can only dispense product after payment! \n")

    def return_change(self):
        print(f"No payment is done to return the change! \n")
