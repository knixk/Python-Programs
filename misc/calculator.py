# Calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    # already made sure to avoid division by zero
    return n1 / n2


# dictionary with references to the functions as values
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# ans = operations["+"](23, 23)
# ans1 = operations["-"](23, 23)
# ans2 = operations["/"](23, 23)
# ans3 = operations["*"](23, 23)

# print(ans, ans1, ans2, ans3)

print("welcome to our calculator...")


def calc():
    num1 = int(input("Enter first digit..."))
    num2 = int(input("Enter second digit..."))
    operator = input("Enter the operator... +, -, /, *")
    ans = operations[operator](num1, num2)
    print("your ans is...", ans)


while (1):

    calc()

    prmpt = input('''would you like to procceed with current sum (y) or start a new calc (n) or exit (e)..?''')

    match prmpt:
        case "y":
            print("y")
            calc()
        case "n":
            print("n")
            calc()
        case "e":
            print("e")
            break
        case _:
            print("Invalid key...")
            

