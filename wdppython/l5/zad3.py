from duze_cyfry import cyfry
from random import choice

import turtle
turtle.penup()          
turtle.goto(-400,400) 
turtle.pendown()            



print(list(cyfry[3]))
def draw_filled_square(color, side_length):
    turtle.begin_fill()
    turtle.color(color)

    for _ in range(4): 
        turtle.forward(side_length)  
        turtle.right(90)

    turtle.end_fill()     

def drawnum(n,side_length):
    kolor = choice([
    "black", "red", "green", "blue", "yellow", "purple", "cyan", "magenta", "orange", "pink", "brown", "gray",
    "gold", "silver", "navy", "lime", "teal", "maroon", "violet", "turquoise", "coral", "indigo", "khaki", "lavender",
    "salmon", "seashell", "wheat", "plum", "orchid", "tomato", "crimson", "darkred", "darkblue", "darkgreen", 
    "darkorange", "darkviolet", "skyblue", "saddlebrown", "lightblue", "lightgreen", "lightyellow", "lightpink", 
    "slateblue", "snow", "forestgreen"
    ])
    cyfra = cyfry[int(n)][1:-1]
    for i in cyfra:
        if i == "\n":
            turtle.penup()
            turtle.right(180)
            turtle.forward(side_length*5)
            turtle.left(90)
            turtle.forward(side_length)
            turtle.left(90)
            turtle.pendown

        elif i == " ":
            draw_filled_square("white",side_length)
            turtle.penup()
            turtle.forward(side_length)
            turtle.pendown
        elif i == "#":
            draw_filled_square(kolor,side_length)
            turtle.penup()
            turtle.forward(side_length)
            turtle.pendown
        else:
            print("whaat")
    turtle.penup()
    turtle.left(90)
    turtle.forward(side_length*4)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.pendown
turtle.speed("fastest")

k = "12312312368"
for i in k:
    drawnum(i,10)
input()