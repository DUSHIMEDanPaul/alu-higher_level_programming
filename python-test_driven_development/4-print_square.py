#!/usr/bin/python3
def print_square(size):
    """ 
    the following function print a square with each size equal to #
    """
    if type (size) is not int:
        raise TypeError("size must  be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if type (size) is float and type(size)<0 :
        raise TypeError("size must be an integer")
    print(("#" * size + "\n") * size, end="")
