from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.forward(-10)


def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
