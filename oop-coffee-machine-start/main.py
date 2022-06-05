from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = MoneyMachine()
maker = CoffeeMaker()
menu = Menu()
isOn = True

while isOn:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        maker.report()
        machine.report()
    else:
        drink = menu.find_drink(choice)
        if maker.is_resource_sufficient(drink):
            if machine.make_payment(drink.cost):
                maker.make_coffee(drink)
