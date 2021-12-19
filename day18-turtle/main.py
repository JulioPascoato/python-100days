import turtle
from turtle import Turtle, Screen
from random import randint, choice


timmy = Turtle()
timmy.shape("turtle")
timmy.color("MidnightBlue")
timmy.speed("fastest")
# timmy.pensize(10)

screen = Screen()
screen.colormode(255)

# # ########### Challenge 1
# # draw square
# for n in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# # ########## Challenge 2
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# # ############ Challenge 3
# for vertices in range(3, 10):
#     timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     for draw in range(vertices):
#         timmy.forward(100)
#         timmy.right(360 / vertices)


# # ############# Challenge 4
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
#
#
# for _ in range(200):
#     timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     timmy.forward(30)
#     timmy.setheading(choice(directions))

# # ########## Challenge 5
# angle = 0
# steps = 5
#
# for _ in range(1, round(360 / steps) + 1):
#     timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     timmy.setheading(angle)
#     timmy.circle(124)
#     angle += steps
#


















screen.exitonclick()