from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
while is_on:
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if menu.find_drink(user_choice):
            user_selection_item = menu.find_drink(user_choice)
            if coffee_maker.is_resource_sufficient(user_selection_item):
                money_machine.make_payment(user_selection_item.cost)
                coffee_maker.make_coffee(user_selection_item)
