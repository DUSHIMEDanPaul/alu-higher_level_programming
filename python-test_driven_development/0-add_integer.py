#!/usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(:"a must be an integer or float and b must be an integer or float")
    a = int(a)
    b = int(b)
    return a + b


