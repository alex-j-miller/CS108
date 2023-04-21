"""CS 108 - Lab 3.3

@author: Alex Miller (ajm94)
@author: Josh Burr (jtb33)
@date: Fall, 2021
"""

from guizero import App, Drawing

app = App('Drawing Canvas')

drawing = Drawing(app, width='fill', height='fill')

# Put your solution code here, replacing this sample line.
#drawing.line(100, 100, 250, 100, color='black')


unit = 50                # Change this value to rescale the drawing.

#drawing head
drawing.oval(
    1 * unit, 2 * unit,  # bounding box x1, y1
    3 * unit, 4 * unit,  # bounding box x2, y2
    outline=True,
    color='white'
    )

#drawing body 
drawing.line(
    2 * unit, 6 * unit,  # x1, y1
    2 * unit, 4 * unit,  # x2, y2
    color='red'
)

#drawing arms 
drawing.line(
    1 * unit, 5 * unit, # x1, y1
    3 * unit, 5 * unit, # x2, y2
    color='black'
)

#drawing leg right
drawing.line(
    2 * unit, 6 * unit, # x1, y1
    3 * unit, 7 * unit, # x2, y2
    color='black'
)

#drawing leg left
drawing.line(
    2 * unit, 6 * unit, # x1, y1
    1 * unit, 7 * unit, # x2, y2
    color='black'
)


app.display()

