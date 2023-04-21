"""CS 108 - Lab/Homework X.X

Describe the module here. Fix the lab number above and the name/date below.
Delete the second @author line if working solo.

@author: YOUR-NAME (yourid123)
@author: PARTNER-NAME (theirid123)
@date: semester, year
"""

import turtle

# Start the turtle window in the corner of the screen (helpful for dual monitor).
# turtle.setup(width=800, height=600, startx=100, starty=100)

window = turtle.Screen()
pen = turtle.Turtle()

unit = 50

#draw head
pen.circle(unit)
pen.right(90)

# Draw torso
pen.forward(unit)

#arms
pen.right(90)
pen.forward(unit)
pen.right(180)
pen.forward(unit * 2)
pen.right(180)
pen.forward(unit)
pen.left(90)
pen.forward(unit)

#legs
pen.right(45)
pen.forward(unit)
pen.right(180)
pen.forward(unit)
pen.right(90)
pen.forward(unit)

# window.mainloop() # Needed for some IDEs.
