"""CS 108 - Lab 7.1

Social Security Number Validation

@author: Alex Miller (ajm94)
@date: Fall, 2021
"""

def is_valid_ssn(ssn):
    ssn_list = ssn.split('-')
    #Test to see if it follows all of the requirements
    if ssn_list[0].isdigit() and ssn_list[1].isdigit() and ssn_list[2].isdigit() and ssn.count('-') == 2 and len(ssn_list[0]) == 3 and len(ssn_list[1]) == 2 and len(ssn_list[2]) == 4:
        return True
    else:
        return False