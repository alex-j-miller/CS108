"""CS 108 - Lab 3.1

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""
#get info
f_name = input('First name: ')
l_name = input('Last name: ')
student_id = input('Student ID: ')

#make login
login = (f_name[0] + l_name + student_id[0] + student_id[1])
login = login.lower()

print('User ID:', login)
