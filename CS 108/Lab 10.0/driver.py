"""CS 108 Lab 10

This driver uses the Employee class to compute and save corporate statistics.

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

from employee import Employee

employees = []

# Construct an employee object for each employee specified in 'employees.txt'
# and add it to the employees list.
# YOUR CODE HERE
f = open('employees.txt', 'r')
while True:
    line = f.readline()
    line = line.split(',')
    if line == ['']:
        break
    employees.append(Employee(line[0], line[1], line[2], int(line[3])))
f.close()
# Write the total number of employees into the 'employee-count.txt' file.
# YOUR CODE HERE
f = open('employee-count.txt', 'w')
f.write(f'{len(employees)}')
f.close()

# Compute and print out statistics for employees
print(len(employees)) # YOU WILL REPLACE THIS LINE.