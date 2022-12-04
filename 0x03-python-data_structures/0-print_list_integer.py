#!/usr/bin/python3
def print_list_integer(my_list=[]):
    my_list.reverse()
    for a in range(0, len(my_list)):
        print("{}".format(my_list.pop()))
        print("\n")
