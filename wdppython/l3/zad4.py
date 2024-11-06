from turtle import *
# rect
penup()
back(300)
rt(90)
fd(200)
rt(270)
pendown()
from random import randint
def rect(h,w=5):
    rt(270)
    fd(h)
    rt(270)
    fd(w)
    rt(270)
    fd(h)
    rt(270)
    fd(w)
speed("fastest")
for i in range(90):
    rect(randint(7*i,8*i)//3)
    penup()
    fd(7)
    pendown()
input()