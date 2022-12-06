#!/usr/bin/python3
def no_c(my_string):
    expempt =['c','C']
    sliced_string = "".join(a for a in my_string if a not in expempt)
    return sliced_string
