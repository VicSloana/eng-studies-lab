my_mood = ["Happy", "Sad", "Sleepy", "Angry"]

import turtle
riley = turtle.Turtle()
riley.width(6)
riley.speed(0)

def draw_start(color):
    for side in range(5):
        riley.forward(100)
        riley.right(144)
        riley.color(color)


def my_mood():
    mood = input("How are you feeling")
    if mood == "Happy":
        print(draw_start(pink))
    elif mood == "Sad":
        print(draw_start(blue))
my_mood()
