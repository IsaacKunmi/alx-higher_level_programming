#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple_of_2 = []
    for a in range(len(my_list)):
        if my_list[a] % 2 == 0:
            multiple_of_2.append(my_list[a])

        return multiple_of_2
