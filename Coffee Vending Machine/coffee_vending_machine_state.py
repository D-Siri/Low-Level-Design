from abc import ABC, abstractmethod


class CoffeeVendingMachineState(ABC):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    @abstractmethod
    def select_coffee(self, product_id):
        pass

    @abstractmethod
    def make_payment(self, money):
        pass

    @abstractmethod
    def dispense_coffee(self):
        pass

    @abstractmethod
    def return_change(self):
        pass


