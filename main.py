#https://www.phillips.com/detail/damien-hirst/UK010120/16

import turtle as t
import random

color_list = [(199, 163, 104), (150, 97, 58), (107, 151, 174), (152, 56, 80), (128, 174, 150), (42, 100, 133), (62, 124, 100), (217, 202, 112), (148, 31, 49), (174, 146, 59), (199, 132, 145), (79, 153, 99), (193, 87, 105), (53, 56, 103), (216, 177, 186), (131, 39, 34), (194, 84, 70), (57, 56, 41), (82, 35, 41), (223, 178, 167), (121, 125, 149), (84, 152, 164), (33, 56, 83), (173, 203, 187), (177, 197, 201)]
t.colormode(255)
timmy = t.Turtle()
timmy.hideturtle()
for j in range(1,11):
    for i in range(1,11):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    timmy.penup()
    timmy.speed('fastest')
    timmy.setx(0)
    timmy.sety(40*(j))
    timmy.pendown()
    timmy.speed('normal')
    
screen = t.Screen()
screen.exitonclick()