"""CS 108 - Lab 7.0

Name format

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

full_name = input("Full Name: ")

full_name_list = full_name.split()

if len(full_name_list) == 3:
    first_name = full_name_list[0]
    first_initial = first_name[0]
    middle_name = full_name_list[1]
    middle_initial = middle_name[0]
    last_name = full_name_list[2]
    print(last_name + ',', first_initial + '.' + middle_initial + '.')
elif len(full_name_list) == 2:
    first_name = full_name_list[0]
    first_initial = first_name[0]
    last_name = full_name_list[1]
    print(last_name + ',', first_initial + '.')
else:
    print("'" + full_name + "'", 'is a non-standard name.')