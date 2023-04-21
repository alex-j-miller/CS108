"""CS 108 - Lab 3.2

@author: Alex Miller (ajm94)
@author: Josh Burr (jtb33)
@date: Fall, 2021
"""
#set score
score_dict = {'Joe' : 10, 'Tom' : 23, 'Barb' : 13, 'Sue' : 19, 'Sally' : 12}

#print Barb's score
print(score_dict['Barb'])

#Change Sally's score
score_dict['Sally'] = 13

#Delete Tom and his score
del score_dict['Tom']

#Print final score
print(score_dict)