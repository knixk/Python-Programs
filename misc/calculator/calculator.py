from art import logo

print(logo)

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


def calc(num1 = None, useFirst = 0):

    if (useFirst != 1):
        print("inside if")
        num1 = float(input("Enter first digit..."))

    operator = input("Enter the operator... +, -, /, * :")
    num2 = float(input("Enter second digit..."))
    ans = operations[operator](num1, num2)
    print(f"your ans for {num1} {operator} {num2} = {ans} ")

    return ans


ans = calc()


while (1):
    prmpt = input('''would you like to procceed with current sum (y) or start a new calc (n) or exit (e)..?''')

    match prmpt:
        case "y":
            print("y")
            ans = calc(ans, 1)
        case "n":
            print("n")
            ans = calc()
        case "e":
            print("e")
            break
        case _:
            print("Invalid key...")
            continue

