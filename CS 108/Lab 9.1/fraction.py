"""CS 108 - Lab 9.1

Fraction Class

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""
import math

class Fraction:
    
    def __init__(self, numerator, denominator):
        """ Recieves a fraction and keeps track of the numerator and denominator. """
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    
    def __str__(self):
        """ Returns the fraction in a readable form. """
        return f"{self.numerator}/{self.denominator}"
    
    def is_valid(self):
        """ Checks to see if the fraction is valid. """
        if self.denominator == 0:
            return False
        else:
            return True
    
    def simplify(self):
        """ Simplifies the fraction. """
        gcd = math.gcd(self.numerator, self.denominator)
        if gcd != 0:
            self.numerator = self.numerator // gcd
            self.denominator = self.denominator //gcd
        if self.denominator < 0:
            self.numerator = self.numerator * -1
            self.denominator = self.denominator * -1
    
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def get_decimal_value(self):
        return self.numerator / self.denominator