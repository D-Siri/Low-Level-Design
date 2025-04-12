from dispense_state import DispenseState
from select_item_state import SelectItemState
from return_change_state import ReturnChangeState
from start_state import StartState
from vending_machine_state import VendingMachineState
from products_inventory import ProductsInventory


class VendingMachine:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.inventory = ProductsInventory()
            cls.instance.total_amount = 0
            cls.instance.current_state = StartState(cls.instance)
            cls.instance.dispense_state = DispenseState(cls.instance)
            cls.instance.start_state = StartState(cls.instance)
            cls.instance.return_change_state = ReturnChangeState(cls.instance)
            cls.instance.accept_item_state = SelectItemState(cls.instance)
            cls.instance.selected_product = None
        return cls.instance

    def set_state(self, state: VendingMachineState):
        self.current_state = state

    def get_amount(self):
        return self.total_amount

    def set_amount(self, value):
        self.total_amount = value

    def get_product(self, product):
        return self.inventory[product]

    def update_inventory(self, product, count):
        self.inventory.products[product] = count

    def insert_money(self, value):
        self.current_state.insert_money(value)

    def select_product(self, product_id):
        self.set_state(self.accept_item_state)
        self.current_state.select_product(product_id)

    def dispense_product(self):
        self.current_state.dispense_product()

    def return_change(self):
        self.set_state(self.return_change_state)
        self.current_state.return_change()
