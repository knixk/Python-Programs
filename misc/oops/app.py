# from turtle import Turtle, Screen

# my_turtle = Turtle()
# my_screen = Screen()

# def move():
#     # Creates a hexagon
#     my_turtle.shape("turtle")
#     my_turtle.color("cyan")
#     my_turtle.forward(50)
#     my_turtle.left(50)
#     my_turtle.forward(50)
#     my_turtle.left(50)
#     my_turtle.forward(50)
#     my_turtle.left(50)
#     my_turtle.forward(50)
#     my_turtle.left(50)
#     my_turtle.forward(50)
#     my_turtle.left(50)
#     my_turtle.forward(50)
#     my_turtle.left(50)
#     my_turtle.forward(50)
#     my_turtle.left(50)


# my_screen.exitonclick()

# -- pt
from prettytable import PrettyTable
table = PrettyTable()
# table.field_names = ["Name", "Age", "Height"]
table.add_column("Name", ["Some", "More", "values"])
table.add_column("Age", ["12", "23", "32"])
table.add_column("Height", ["122", "123", "132"])
table.align = "r"
print(table)
