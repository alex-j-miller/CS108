"""CS 108 - Lab 4.0

Automobile service Cost

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

service = input('service: ')

if service == 'oil change':
    print('cost of oil change: $35')
elif service == 'tire rotation':
    print('cost of tire rotation: $19')
elif service == 'car wash':
    print('cost of car wash: $7')
else:
    print('error:', service, 'is not recognized')