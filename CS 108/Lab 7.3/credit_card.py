"""CS 108 - Lab 7.3

Credit Card Number Validation

@author: Alex Miller (ajm94)
@author: Jaden Brookens (jlb224)
@date: Fall, 2021
"""

def is_valid_prefix(inp):
    '''Checks to see if a CC has a valid prefix'''
    if int(inp[0]) == 3 and int(inp[1]) == 7:
        return True
    elif int(inp[0]) == 4 or int(inp[0]) == 5 or int(inp[0]) == 6:
        return True
    else:
        return False

def sum_of_odds(inp):
    '''Adds together the odd digits starting from the right'''
    sum = 0
    for i in range(-1, -1 * len(inp) - 1, -2):
        sum += int(inp[i])
    return sum

def sum_of_double_evens(inp):
    '''Doubles all of the even digits starting at the right and add them together'''
    sum = 0
    even = []
    for i in range(-2, -1 * len(inp) - 1, -2):
        even.append(str(2 * int(inp[i])))
    for i in range(len(even)):
        if len(even[i]) == 2:
            even[i] = str(int(even[i][0]) + int(even[i][1]))
    for i in range(len(even)):
        sum += int(even[i])
    return sum

def is_valid_cc(cc):
    '''Test to see if the CC number that is recieves is valid'''
    if is_valid_prefix(cc) and 13 <= len(cc) <= 16 and cc.isdigit() and (sum_of_odds(cc) + sum_of_double_evens(cc)) % 10 == 0:
        return True
    else:
        return False
    
print(is_valid_cc('4716296048457411'))