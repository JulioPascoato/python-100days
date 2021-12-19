# ##This code will not work in repl.it as there is no access to the colorgram package here.###
# #We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color. rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.colormode(255)


turtle = Turtle()
turtle.pensize(20)
turtle.speed(0)

color_list = [(196, 160, 119), (71, 92, 126), (144, 86, 57), (216, 210, 119), (140, 160, 189), (183, 146, 162),
              (29, 32, 46), (175, 160, 39), (121, 72, 92), (57, 35, 25), (138, 174, 153), (78, 116, 79), (61, 31, 40),
              (141, 26, 17), (123, 27, 40), (185, 99, 85), (47, 59, 93), (176, 97, 113), (99, 119, 171), (33, 51, 45),
              (101, 156, 86), (215, 175, 189), (216, 180, 174), (67, 84, 27), (162, 208, 188), (180, 187, 213)]

turtle.penup()


for y in range(0, 10):
    for x in range(0, 10):
        turtle.dot(20, choice(color_list))
        turtle.setposition(50 * x, 50 * y)

turtle.dot(20, choice(color_list))
turtle.hideturtle()

screen.exitonclick()