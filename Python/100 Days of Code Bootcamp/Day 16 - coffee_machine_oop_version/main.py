#Ioannis Apomachos

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_options=menu.get_items()
keep_operating=True

while keep_operating!="off":
    user_choice=input(f"What would you like? {menu_options}: ")
    if user_choice=="report":
        coffee_maker.report()
        money_machine.report()

    elif user_choice=="espresso" or user_choice=="latte" or user_choice=="cappuccino":
        drink=menu.find_drink(user_choice)
        resources_status=coffee_maker.is_resource_sufficient(drink)
        if resources_status:
            inserted_money=money_machine.make_payment(drink.cost)
            if inserted_money:
               coffee_maker.make_coffee(drink)

     
    elif user_choice=="off":
        keep_operating="off"
