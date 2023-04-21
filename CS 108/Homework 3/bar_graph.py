"""CS 108 - Homework 5.2

Bar Graphs

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""
import random
from guizero import App, Drawing
app = App('Drawing Canvas')

def get_data():
    '''Recieves numbers from user and puts it into a list.'''
    x = []
    print('Please enter the data elements to graph.')
    while True:
        value = float(input('integer (negative number to quit): '))
        if value < 0:
            print('Please enter at least one value')
        else:
            while True:
                if value < 0:
                    return x
                else:
                    x.append(value)
                value = float(input('integer (negative number to quit): '))

def get_random_color():
    '''Selects a random color.'''
    return random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_bar_graph():
    '''Draws a bar graph from a list of numbers.'''
    drawing = Drawing(app, width='fill', height='fill')
    num_list = get_data()
    multiplier =  drawing.master.width / max(num_list)
    y_diff = drawing.master.height / len(num_list)
    prev_y = 0
    #Draws the bar graphs
    for i in range(len(num_list)):
        new_y = prev_y + y_diff
        x2 = num_list[i] * multiplier
        drawing.rectangle(0, prev_y, x2, new_y, color= get_random_color(), outline=True, outline_color= get_random_color())
        prev_y = new_y

draw_bar_graph()
app.display()
