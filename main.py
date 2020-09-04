import turtle
import time
import random

# Setting up objects
window = turtle.Screen()
head = turtle.Turtle()
food = turtle.Turtle()
segments = []

# FUNCTIONS

def move():
    ycor = head.ycor()
    xcor = head.xcor()

    if head.direction == "up":
        head.goto(xcor, ycor + 20)
    if head.direction == "down":
        head.goto(xcor, ycor - 20)
    if head.direction == "left":
        head.goto(xcor - 20, ycor)
    if head.direction == "right":
        head.goto(xcor + 20, ycor)

def go_up():
    if(head.direction != "down"):
        head.direction = "up"

def go_right():
    if(head.direction != "left"):
        head.direction = "right"

def go_down():
    if(head.direction != "up"):
        head.direction = "down"

def go_left():
    if(head.direction != "right"):
        head.direction = "left"

def randomize_pos():
    randX = random.randint(-290, 290)
    randY = random.randint(-290, 290)
    food.goto(randX,randY)

def check_touching():
    if(head.distance(food) < 15):
        randomize_pos()

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

def segment_movement():

    if len(segments) > 0:
        xpos = head.xcor()
        ypos = head.ycor()

        segments[0].goto(xpos, ypos)

    for index in range(len(segments) - 1, 0, -1):
        xpos = segments[index - 1].xcor()
        ypos = segments[index - 1].ycor()

        segments[index].goto(xpos, ypos)


# Initializing window
window.title("My Snake Game")
window.screensize(600, 600)
window.bgcolor("green")
window.tracer(0)

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_right, "d")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")

# Initializing head
head.goto(0,0)
head.penup()
head.shape("square")
head.direction = "up"

# Initializing food
food.penup()
food.shape("circle")
food.color("red")
food.shapesize(0.5,0.5)
randomize_pos()

# Initializing other variables
delay = 0.1

while True:
    window.update()
    segment_movement()
    move()
    check_touching()

    time.sleep(delay)