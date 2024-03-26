#!/usr/bin/python3

def add_integer(a, b=98):
<<<<<<< HEAD
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(:"a must be an integer or float and b must be an integer or float")
=======
    def add_numbers(a, b):
     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or float and b must be an integer or float")
>>>>>>> 43619936b2ef55d5bd4f745ce36123b8ecb2d424
    a = int(a)
    b = int(b)
    return a + b


