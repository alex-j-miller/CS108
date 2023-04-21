"""CS 108 - Lab 2.2

Turtle Stick Figure

@author: Alex Miller (ajm94)
@author: Jaden Brookens (jlb224)
@date: Fall, 2021
"""

import turtle
import math

# Start the turtle window in the corner of the screen (helpful for dual monitor).
# turtle.setup(width=800, height=600, startx=100, starty=100)

window = turtle.Screen()
pen = turtle.Turtle()

UNIT = 50

#draw head
pen.circle(UNIT)
pen.right(90)

#draw arms and body
pen.forward(UNIT)
pen.right(90)
pen.forward(UNIT)
pen.right(180)
pen.forward(UNIT * 2)
pen.right(180)
pen.forward(UNIT)
pen.left(90)
pen.forward(UNIT)

#draw legs
pen.right(45)
pen.forward(math.sqrt(2 * (UNIT ** 2)))
pen.right(180)
pen.forward(math.sqrt(2 * (UNIT ** 2)))
pen.right(90)
pen.forward(math.sqrt(2 * (UNIT ** 2)))


