from vending_machine_state import VendingMachineState


class ReturnChangeState(VendingMachineState):

    def insert_money(self, money):
        print(f"cannot insert the money now, Start a new transaction!")

    def select_product(self, product_id):
        print(f"No available balance to select the product")

    def dispense_product(self):
        print(f"insufficient funds,No Product can be dispensed at this time!")

    def return_change(self):
        if self.vending_machine.get_amount() > 0:
            print(f"please collect your change of {self.vending_machine.total_amount}")
            self.vending_machine.set_amount(0)
        else:
            print(f"No change left to return. All the amount inserted is exhausted!")
        self.vending_machine.set_state(self.vending_machine.start_state)
