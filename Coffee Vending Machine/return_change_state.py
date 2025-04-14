from coffee_vending_machine_state import CoffeeVendingMachineState
from ProductsInventory import ProductsInventory


class ReturnChangeState(CoffeeVendingMachineState):

    def select_coffee(self, coffee):
        pass

    def make_payment(self, money):
        pass

    def dispense_coffee(self):
        print(f"Can only dispense product after payment! \n")

    def return_change(self):
        amount = self.vending_machine.get_amount()
        if amount > 0:
            print(f"take your change of {amount}$ \n")
            self.vending_machine.set_amount(0)
