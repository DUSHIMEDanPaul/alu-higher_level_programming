#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function adds two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    else:
           return (int(a) + int(b))

#!/usr/bin/python3
import doctest

def add(a, b=98):
    """
    This function adds two integers.
    
    >>> add(3, 98)
    101
    """
    return a + b

if __name__ == "__main__":
     import doctest
     doctest.testmod()

