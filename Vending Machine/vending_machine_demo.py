from vending_machine import VendingMachine
from product import Product
from price_value import Price


vending_machine = VendingMachine()
a = Product(1, 1)
b = Product(1, 2)
c = Product(3, 3)

vending_machine.inventory.add_product(a)
vending_machine.inventory.add_product(b)
vending_machine.inventory.add_product(c)

vending_machine.insert_money(Price.DIME.value)
vending_machine.insert_money(Price.NICKLE.value)
vending_machine.insert_money(Price.FIVE.value)

vending_machine.select_product(a)
vending_machine.return_change()
