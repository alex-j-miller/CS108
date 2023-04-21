"""CS 108 - Homework 5

Bar Graphs

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

from bar_graph import BarGraph

def get_data():
    filename = input('Filename: ')
    f = open(filename, 'r')
    data = []
    while True:
        g = f.readline().strip()
        if g == '':
            break
        data.append(int(g))
    f.close()
    return data

bg = BarGraph(get_data(), 'blue')