from turtle import Turtle, Screen
from prettytable import PrettyTable

# bugi = Turtle() # object = class
#
# print(bugi)
#
# # object.method
# bugi.shape("turtle")
# bugi.color("blue")
# bugi.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight) #object.attribute
# my_screen.exitonclick()
#



table = PrettyTable()
table.add_column('Pokemon name', ["Pikachu", "Squirtle", "Charmander"])
table.add_column('Type', ["electric", "water", "fire"])

table.align = 'l'
print(table)



