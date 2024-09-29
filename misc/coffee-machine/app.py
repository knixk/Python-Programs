from time import sleep

resources = {
    "water": 500,
    "milk": 250,
    "coffee": 100
}

profit = 0

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

def is_resources_sufficient(choice):
    print(choice)
    pass

welcome = "welcome to coffee machine"
print(welcome)

is_on = True

while (is_on):
    
    ans = input("what would you like to drink? \n (e) espresso, (l) latte, (c) cappuccino \n >")
    if ans == "off":
        exit()
    elif ans == "report":
        print(resources)    
    elif ans == "e":
        choice = "espresso"
    elif ans == "l":
        choice = "latte"
    elif ans == "c":
        choice = "cappuccino"
    else:
        print("choose a correct option pls..")    
        continue

        
    drink = MENU[choice]
    is_resources_sufficient(drink['ingredients'])
    # print(drink)


# To do
# 1. get user choice
# 2. check if that choice can be made
# 3. show the user price
# 4. ask user to enter the money

# 5. check if it's enough and give the coffee
# 6. ask again