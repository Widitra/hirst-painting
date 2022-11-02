import turtle
from turtle import Turtle, Screen
import random


def draw_dots():
    for _ in range(7):
        t.dot(20, random.choice(color_list))
        t.forward(50)


def initialize_position():
    t.hideturtle()
    t.penup()
    t.setheading(215)
    t.forward(265)
    t.setheading(0)
    draw_dots()


def right_to_left():
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(50)
    draw_dots()


def left_to_right():
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(50)
    draw_dots()


turtle.colormode(255)
t = Turtle()
color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189),
              (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10),
              (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61)]

initialize_position()
for _ in range(3):
    right_to_left()
    left_to_right()

screen = Screen()
screen.exitonclick()
