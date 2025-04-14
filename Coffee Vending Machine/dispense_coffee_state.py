from coffee_vending_machine_state import CoffeeVendingMachineState


class DispenseCoffeeState(CoffeeVendingMachineState):

    def select_coffee(self, coffee):
        pass

    def make_payment(self, money):
        pass

    def dispense_coffee(self):
        tot_cost = self.vending_machine.get_cost()
        tot_amount = self.vending_machine.get_amount()
        if tot_cost <= tot_amount:
            print(f"Dispensed products {self.vending_machine.selected_products} \n")
            self.vending_machine.set_amount(tot_amount-tot_cost)
            self.vending_machine.set_state(self.vending_machine.return_change_state)
            self.vending_machine.selected_products = []
        else:
            print(f"Insufficient Money, Please collect your money and try selecting items again!! \n")
            self.vending_machine.set_state(self.vending_machine.return_change_state)

    def return_change(self):
        print(f"No payment is done to return the change! \n")
