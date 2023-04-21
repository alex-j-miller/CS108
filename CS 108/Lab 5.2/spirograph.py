"""CS 108 - Lab 5.2

Spirograph 

@author: Alex Miller (ajm94)
@author: Jaden Brookens (jlb224)
@date: Fall, 2021
"""

from guizero import App, Drawing
import math

app = App('Drawing Canvas')
drawing = Drawing(app, width='fill', height='fill')

#get inputs from user
moving_radius = float(input('moving radius: '))
fixed_radius = float(input('fixed radius: '))
pen_offset = float(input('pen offset: '))
color = input('color: ')

#get initial values
t = 0
center = 250
x = ((fixed_radius + moving_radius) * math.cos(t)) + pen_offset * math.cos(((fixed_radius + moving_radius) * t) / moving_radius) + center
y = ((fixed_radius + moving_radius) * math.sin(t)) + pen_offset * math.sin(((fixed_radius + moving_radius) * t) / moving_radius) + center
counter = 0
#graph the spirograph
while t < 360:
    t += 0.1
    next_x = ((fixed_radius + moving_radius) * math.cos(t)) + pen_offset * math.cos(((fixed_radius + moving_radius) * t) / moving_radius) + center
    next_y = ((fixed_radius + moving_radius) * math.sin(t)) + pen_offset * math.sin(((fixed_radius + moving_radius) * t) / moving_radius) + center
    drawing.line(x , y, next_x, next_y, color)
    x = next_x
    y = next_y

app.display()