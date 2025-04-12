from abc import ABC, abstractmethod

class VendingMachineState(ABC):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    @abstractmethod
    def select_product(self, product_id):
        pass

    @abstractmethod
    def insert_money(self, money):
        pass

    @abstractmethod
    def dispense_product(self):
        pass

    @abstractmethod
    def return_change(self):
        pass

