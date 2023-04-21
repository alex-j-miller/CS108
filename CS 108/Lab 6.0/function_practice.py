"""CS 108 - Lab 6.0

Function Practice

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

def compute_cost(miles, miles_per_gallon, dollars_per_gallon):
    return (float(miles) / float(miles_per_gallon)) * float(dollars_per_gallon)

def count_spaces(s):
    count = 0
    for c in str(s):
        if c == ' ':
            count += 1
    return count 