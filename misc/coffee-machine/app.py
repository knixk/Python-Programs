from time import sleep

welcome = "welcome to coffee machine"
print(welcome)
sleep(1)

profit = 0
is_on = True

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

def insert_coins():
    """Returns the total sum of the coins inserted"""
    total = int(input("How many quarters? (0.25$) ")) * 0.25
    total += int(input("How many dimes? (0.10$) ")) * 0.10
    total += int(input("How many nickles? (0.05$) ")) * 0.05
    total += int(input("How many pennies? (0.01$) ")) * 0.01
    return total

def is_resources_sufficient(choice):
    """Returns boolean if we have enough resources for the drink to make"""
    # print(choice)
    for item in choice:
        print(item)
        if (choice[item] >= resources[item]):
            return False

    return True

def use_machine():
        
    global profit
    
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

    drink = MENU[choice]
    res = is_resources_sufficient(drink['ingredients'])
    
    if (res):
        print(f"You need to pay {drink['cost']}$ for the drink" )
        coins = insert_coins()
        if (coins < drink['cost']):
            print("You need to add ... more coins")
            
        profit += drink['cost']
        change = round(coins - drink['cost'], 2) 
        # print("Enjoy your drink... ☕")

    if (change > 0):
        print(f"Here is your change... {change}")


while (is_on):
    use_machine()
    

# To do
# 1. get user choice
# 2. check if that choice can be made
# 3. show the user price
# 4. ask user to enter the money
# 5. check if it's enough and give the coffee
# 6. ask again