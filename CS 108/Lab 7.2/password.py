"""CS 108 - Lab 7.2

Password Validation

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

def add_digits(string):
    '''Counts the number of digits in a string'''
    counter = 0
    for i in range(len(string)):
        if string[i].isnumeric():
            counter += 1
    return counter
            

def is_valid_password(pw):
    '''Checks to see if a password is valid'''
    if len(pw) >= 8 and pw.isalnum() and add_digits(pw) >= 2:
        return True
    else:
        return False