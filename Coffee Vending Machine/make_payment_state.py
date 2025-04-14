from coffee_vending_machine_state import CoffeeVendingMachineState
from ProductsInventory import ProductsInventory


class MakePaymentState(CoffeeVendingMachineState):

    def select_coffee(self, coffee):
        pass

    def make_payment(self, amount):
        current_amount = self.vending_machine.get_amount()
        current_amount += amount
        self.vending_machine.set_amount(current_amount)

    def dispense_coffee(self):
        print(f"Can only dispense product after payment! \n")

    def return_change(self):
        print(f"No payment is done to return the change! \n")
