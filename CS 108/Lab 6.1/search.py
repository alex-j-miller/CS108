"""CS 108 - Lab 6.1

Search

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

def search(str_list, target):
    for i in range(len(str_list)):
        if target == str_list[i]:
            return i
    return -1