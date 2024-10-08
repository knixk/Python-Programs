from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("welcome to coffee machine")
my_maker = CoffeeMaker()
my_menu = Menu()
my_money = MoneyMachine()
# my_items = MenuItem()

while True:
    print(my_menu.get_items())
    drink = input("what would u like to drink? ")

    if (drink == 'e'):
        break

    find_drink = my_menu.find_drink(drink)
    cost = find_drink.cost
    can_make = my_maker.is_resource_sufficient(find_drink)


    if (can_make):
        print(f"Please pay {cost}$")
        payment_successful = my_money.make_payment(cost)

        if (payment_successful):
             my_maker.make_coffee(find_drink)
            

    my_maker.report()
    my_money.report()



