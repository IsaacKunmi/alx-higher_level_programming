#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    modified_list = my_list

    if idx < 0:
        return my_list

    elif idx >= len(my_list):
        return my_list

    else:
        modified_list[idx] = element
        return modified_list