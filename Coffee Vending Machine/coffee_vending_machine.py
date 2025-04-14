from select_coffee_state import SelectCoffeeState
from make_payment_state import MakePaymentState
from dispense_coffee_state import DispenseCoffeeState
from return_change_state import ReturnChangeState
from coffee_vending_machine_state import CoffeeVendingMachineState
from ProductsInventory import ProductsInventory
from Coffee import Coffee


class CoffeeVendingMachine:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.total_amount = 0
            cls._instance.inventory = ProductsInventory()
            cls._instance.selected_products = []
            cls._instance.current_state = SelectCoffeeState(cls._instance)
            cls._instance.select_coffee_state = SelectCoffeeState(cls._instance)
            cls._instance.make_payment_state = MakePaymentState(cls._instance)
            cls._instance.dispense_coffee_state = DispenseCoffeeState(cls._instance)
            cls._instance.return_change_state = ReturnChangeState(cls._instance)

        return cls._instance

    def set_state(self, state: CoffeeVendingMachineState):
        self.current_state = state

    def get_cost(self):
        cost = 0
        for item in self.selected_products:
            cost += item.price
        return cost

    def get_amount(self):
        return self.total_amount

    def set_amount(self, amount):
        self.total_amount = amount

    def get_product(self, product):
        return self.inventory[product]

    def update_inventory(self, product, count):
        self.inventory.coffee_inventory[product] = count

    def make_payment(self, value):
        self.set_state(self.make_payment_state)
        self.current_state.make_payment(value)

    def select_coffee(self, product):
        self.set_state(self.select_coffee_state)
        if self.current_state.select_coffee(product):
            self.selected_products.append(product)

    def dispense_coffee(self):
        self.set_state(self.dispense_coffee_state)
        self.current_state.dispense_coffee()

    def return_change(self):
        self.set_state(self.return_change_state)
        self.current_state.return_change()

    def show_available_products(self):
        self.inventory.show_products()
