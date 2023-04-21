"""CS 108 Lab 10

This driver uses the Employee class to compute and save corporate statistics.

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

from employee import Employee
employees = []

# Get info from a text doc
f = open('employees.txt', 'r')
while True:
    line = f.readline()
    line = line.split(',')
    if line == ['']:
        break
    employees.append(Employee(line[0], line[1], line[2], int(line[3])))
f.close()

if len(employees) == 0:
    print('There are no employees.')
else:
    totals = {}
    counts = {}
    max_employee = employees[0]
    min_employee = employees[0]
    for employee in employees:
        if employee.rank in totals:
            totals[employee.rank] += employee.salary
            counts[employee.rank] += 1
        else:
            totals[employee.rank] = employee.salary
            counts[employee.rank] = 1
        if employee.salary > max_employee.salary:
            max_employee = employee
        if employee.salary < min_employee.salary:
            min_employee = employee
print("Maximum and Minimum Salaries")
print(f'{max_employee}\n{min_employee}')
print('Rank and Average Salaries')
for rank in totals:
    print(rank + ': {:.2f}'.format(totals[rank] / counts[rank]))

# Compute and add the employee count to a text doc
f = open('employee-count.txt', 'w')
f.write(f'{len(employees)}')
f.close()