from time import sleep

resources = {
    "water": 500,
    "milk": 250,
    "coffee": 100
}

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


welcome = "welcome to coffee machine"
print(welcome)

# sleep(1)
# exit()
ans = input("what would you like to drink? \n (e) espresso, (l) latte, (c) cuppucinno \n >")

if (ans == 'e'):
    item = MENU["espresso"]["ingredients"]
    if (resources['coffee'] >= item['coffee']):
        pass
    if (resources['mlik'] >= item['mlik']):
        pass
    if (resources['mlik'] >= item['mlik']):
        pass
    
    
    # print(MENU["espresso"]["ingredients"])
    pass
elif (ans == 'l'):
    pass
elif (ans == 'c'):
    pass
else:
    pass


# 1. get user choice
# 2. check if that choice can be made
# 3. show the user price
# 4. ask user to enter the money

# 5. check if it's enough and give the coffee
# 6. ask again