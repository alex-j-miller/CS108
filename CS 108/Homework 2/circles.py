""" CS 108 - Homework 2

Canvas Circles

@author: Alex Miller (ajm94)
@author: Jaden Brookens (jlb224)
@date: Fall, 2021
"""
#setting up the canvas
from guizero import App, Drawing
app = App('Drawing Canvas')
drawing = Drawing(app, width='fill', height='fill')

#getting values for the first circle
x1 = int(input('Circle 1 x:'))
y1 = int(input('Circle 1 y:'))
r1 = int(input('Circle 1 radius:'))

#getting values for the second circle
x2 = int(input('Circle 2 x:'))
y2 = int(input('Circle 2 y:'))
r2 = int(input('Circle 2 radius:'))

#drawing the circles
drawing.oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, color="white", outline=True)
drawing.oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, color="white", outline=True)

#calculating the distance between the centers of the circles
dist = ((((y2 - y1) ** 2) + ((x2 - x1) ** 2) )** 0.5)

#testing to see if the circles are disjointed or contain one anther or just overlapping
if dist > (r1 + r2):
    drawing.text(0, 0, 'The circles are disjoint.', color='black')
    print('The circles are disjoint.')
elif dist + r1 < r2:
    drawing.text(0, 0, 'Circle 2 contains circle 1.', color='black')
    print('Circle 2 contains circle 1.')
elif dist + r2 < r1:
    drawing.text(0, 0, 'Circle 1 contains circle 2.', color='black')
    print('Circle 1 contains circle 2.')
else:
    drawing.text(0, 0, 'The circles overlap.', color='black')
    print('The circles overlap.')

app.display()