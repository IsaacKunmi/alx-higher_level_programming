#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    multiple_of_2 = []
    if my_list is None:
        for a in my_list:
            if my_list[a] % 2 == 0:
                multiple_of_2.append(True)
            return multiple_of_2
    else:
        multiple_of_2.append(False)
    return multiple_of_2
