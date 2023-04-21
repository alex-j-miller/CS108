"""CS 108 - Homework 5

Bar Graphs

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""
import random
from guizero import App, Drawing

class BarGraph:
    
    def get_data(self):
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

    def get_random_color(self):
        '''Selects a random color.'''
        return random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

    def draw_bar_graph(data, color):
        '''Draws a bar graph from a list of numbers.'''
        app = App('Drawing Canvas')
        drawing = Drawing(app, width='fill', height='fill')
        multiplier =  drawing.master.width / max(data)
        y_diff = drawing.master.height / len(data)
        prev_y = 0
        #Draws the bar graphs
        for i in range(len(data)):
            new_y = prev_y + y_diff
            x2 = data[i] * multiplier
            drawing.rectangle(0, prev_y, x2, new_y, color= color)
            prev_y = new_y
        app.display()
        
    def __init__(self, data, color='blue'):
        self.data = data
        self.color = color
        
        BarGraph.draw_bar_graph(self.data, self.color)
        
    def __str__(self):
        return f'Bar Graph - Color: {self.color} Data: {self.data}'
    
