''' Final Project - Cards

Sets the class for Uno Cards

@author: Alex Miller (ajm94)
@date: Fall, 2021
'''

class Card:
    
    def __init__(self, color, num):
        self.color = color
        self.num = num
    
    def __str__(self):
        self.words()
        return f"{self.w_color} {self.w_num}"
    
    def words(self):
        if self.color == 'G':
            self.w_color = 'Green'
        elif self.color == 'R':
            self.w_color = 'Red'
        elif self.color == 'B':
            self.w_color = 'Blue'
        elif self.color == 'Y':
            self.w_color = 'Yellow'
        elif self.color == 'W':
            self.w_color = 'Wild'
            
        if self.num == '+':
            if self.color == 'W':
                self.w_num = '+4'
            else:
                self.w_num = '+2'
        elif self.num == 'S':
            self.w_num = 'Skip'
        elif self.num == 'R':
            self.w_num = 'Reverse'
        else:
            self.w_num = self.num
        