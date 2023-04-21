"""CS 108 - Lab 2.1

Einstein's Number Puzzle

@author: Alex Miller (ajm94)
@author: Jaden Brookens (jlb224)
@date: Fall, 2021
"""
#get number from an input
number = input()

#get all the correct digits
digit1 = number[0]
digit2 = number[1]
digit3 = number[2]

#setting the reverse number
rev_number = digit3 + digit2 + digit1

#getting the difference
difference = abs(int(number) - int(rev_number))

#setting the difference to a string
difference = str(difference)

#getting the digits of the difference
digit1 = difference[0]
digit2 = difference[1]
digit3 = difference[2]

#setting the reverse difference
rev_diff = digit3 + digit2 + digit1

#printing the output
print("Number:", int(difference) + int(rev_diff))