#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple_of_2 = []
    for a in my_list:
        if a % 2 == 0:
            multiple_of_2.append(True)
        else:
            multiple_of_2.append(False)
    return multiple_of_2
