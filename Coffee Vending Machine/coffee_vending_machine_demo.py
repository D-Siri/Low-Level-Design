from CoffeeRecipe import CoffeeRecipe
from CappuccinoCoffee import CappuccinoCoffee
from EspressoCoffee import EspressoCoffee
from LatteCoffee import LatteCoffee
from coffee_vending_machine import CoffeeVendingMachine


cappuccino_recipe = CoffeeRecipe()
cappuccino_recipe.add_ingredients("Espresso", 1)
cappuccino_recipe.add_ingredients("Steamed Milk", 1)
cappuccino_recipe.add_ingredients("Foamed Milk", 1)

latte_recipe = CoffeeRecipe()
latte_recipe.add_ingredients("Espresso", 1)
latte_recipe.add_ingredients("Steamed Milk", 2)

espresso_recipe = CoffeeRecipe()
espresso_recipe.add_ingredients("Espresso", 2)

cappuccino = CappuccinoCoffee()
cappuccino.set_price(5)
cappuccino.set_recipe(cappuccino_recipe)

latte = LatteCoffee()
latte.set_price(4)
latte.set_recipe(latte_recipe)

espresso = EspressoCoffee()
espresso.set_price(3)
espresso.set_recipe(espresso_recipe)

print("Cappuccino Price:", cappuccino.get_price())
print("Cappuccino Recipe:", dict(cappuccino.recipe.items))
print("\nLatte Price:", latte.get_price())
print("Latte Recipe:", dict(latte.recipe.items))
print("\nEspresso Price:", espresso.get_price())
print("Espresso Recipe:", dict(espresso.recipe.items))

machine = CoffeeVendingMachine()
machine.inventory.add_product(espresso)
machine.inventory.add_product(latte)
machine.inventory.add_product(cappuccino)
machine.show_available_products()

machine.select_coffee(espresso)

machine.make_payment(10)

machine.dispense_coffee()

machine.return_change()

machine.show_available_products()
