from turtle import Turtle
from random import randint

fabio = Turtle()
isabel = Turtle ()
manuel = Turtle ()
daniela = Turtle ()

fabio.shape("turtle")
fabio.color("red")
isabel.shape("turtle")
isabel.color("green")
manuel.shape("turtle")
manuel.color("blue")
daniela.shape("turtle")
daniela.color("purple")

fabio.penup()
fabio.goto(-160,100)
fabio.pendown()

isabel.penup()
isabel.goto(-160,70)
isabel.pendown()

manuel.penup()
manuel.goto(-160,40)
manuel.pendown()

daniela.penup()
daniela.goto(-160,10)
daniela.pendown()

for movement in range (100):
    fabio.forward(randint(1,5))
    isabel.forward(randint(1,5))
    manuel.forward(randint(1,5))
    daniela.forward(randint(1,5))