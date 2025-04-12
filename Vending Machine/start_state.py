from vending_machine_state import VendingMachineState

class StartState(VendingMachineState):

    def __init__(self, vending_machine):
        super().__init__(vending_machine)
        self.vending_machine = vending_machine

    def insert_money(self, value):
        amount = self.vending_machine.get_amount()
        amount += value
        self.vending_machine.set_amount(amount)
        print(f"Received {value}$ amount")

    def select_product(self, product_id):
        print(f"cannot select product while inserting money")

    def dispense_product(self):
        print(f"Cannot dispense product without selecting any product")

    def return_change(self):
        print("cannot return change without selecting any product")
