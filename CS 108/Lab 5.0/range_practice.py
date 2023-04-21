"""CS 108 - Lab 5.0

Output range with increment of 10

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""
#Get inputs
num1 = int(input())
num2 = int(input())

#Check for valid inputs
if num1 > num2:
    print("Second integer can't be less than the first.")
else:
    #Print multiples of 10
    for i in range(num1, num2 + 1, 10):
        print(i)