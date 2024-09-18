from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

screen = Screen()
screen.colormode(255)  # Set colormode on the screen object
#screen.bgcolor("black")

t = Turtle()
t.shape("arrow")
t.speed('fastest')
t.pensize(2)  # Reduced pensize for better visibility
t1 = Turtle()
t1.shape("arrow")
t1.speed('fastest')
t1.pensize(2)  # Reduced pensize for better visibility

for _ in range(36):  # Create a full spirograph
    t.color(random_color())
    t1.color(random_color())
    t1.circle(100)
    t.circle(100)
    t.left(20)  # Rotate x degrees after each circle
    t1.right(20)  # Rotate x degrees after each circle
    

screen.exitonclick()