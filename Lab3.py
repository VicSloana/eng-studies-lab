#The authors are Maggie and Victoria

import turtle
fred = turtle.Turtle()
fred.color("red")
fred.forward(100)
fred.right(135)
fred.forward(140)
fred.right(135)
fred.forward(100)

import turtle
fred = turtle.Turtle()
fred.color("red")
fred.forward(100)
fred.right(90)
fred.forward(140)
fred.right(135)
fred.forward(100)

fred = turtle.Turtle()
fred.color("cyan")
fred.forward(100)
fred.right(90)
fred.color("green")
fred.forward(100)
fred.right(90)
fred.color("blue")
fred.forward(100)
fred.right(90)
fred.color("gold")
fred.forward(100)

import math
def kgr(lb):
    result = lb * 2.2046244202
    print(lb, "lb is", result, "kgr")

kgr(10)

def km(m):
    result = m * 0.6213688756
    print(m, "m is", result, "km")

km(15)

def m(ft):
    result = ft * 3.280839895
    print(ft, "ft is", result, "ft")

m(20)

def song():
    lyrics = "Yesterday, all my trouble seemed so far away, now it looks as though they're here to stay, oh I believe in yesterday"
    print(lyrics)
    print(lyrics)
    print(lyrics)

song()

def song_2(x):
    lyrics = "Yesterday, all my trouble seemed so far away, now it looks as though they're here to stay, oh I believe in yesterday, \n"
    print(lyrics * x)

song_2(3)
