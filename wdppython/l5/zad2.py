import turtle
import random

turtle.speed("fastest") 
turtle.width(2) 

def draw_branch(t, branch_length, angle, depth):
    if depth > 0:
        random_angle = angle + random.randint(-10, 10)
        random_length = branch_length * (0.9 + random.uniform(0, 0.1))
        t.forward(random_length)

        t.right(random_angle)
        draw_branch(t, random_length, angle, depth - 1)  

        t.left(2 * random_angle)
        draw_branch(t, random_length, angle, depth - 1)
        t.right(random_angle)
        t.backward(random_length)

turtle.left(90) 
turtle.penup()
turtle.goto(0, -250) # Move to the bottom of the screen
turtle.pendown()

draw_branch(turtle, branch_length=70, angle=25, depth=8)


input()# Keep the window open until closed