"""CS 108 - Homework 2.12

Turtle Flag

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

import turtle

window = turtle.Screen()
pen = turtle.Turtle()

unit = 50

#blue part of flag
pen.color("#0055A4")
pen.begin_fill()
pen.forward(unit)
pen.right(90)
pen.forward(unit * 2)
pen.right(90)
pen.forward(unit)
pen.right(90)
pen.forward(unit * 2)
pen.end_fill()
pen.right(90)
pen.forward(unit)

#white part of flag
pen.color("#FFFFFF")
pen.begin_fill()
pen.forward(unit)
pen.right(90)
pen.forward(unit * 2)
pen.right(90)
pen.forward(unit)
pen.right(90)
pen.forward(unit * 2)
pen.end_fill()
pen.right(90)
pen.forward(unit)

#red part of flag
pen.begin_fill()
pen.color("#EF4135")
pen.forward(unit)
pen.right(90)
pen.forward(unit * 2)
pen.right(90)
pen.forward(unit)
pen.right(90)
pen.forward(unit * 2)
pen.right(90)
pen.end_fill()