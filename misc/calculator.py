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


ans = operations["+"](23, 23)
ans1 = operations["-"](23, 23)
ans2 = operations["/"](23, 23)
ans3 = operations["*"](23, 23)

print(ans, ans1, ans2, ans3)