# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
#
# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# my_screen.exitonclick()
#
#
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Picachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("Test", [1, 2, 3])

print(table.align)
table.align = "l"

print(table)



