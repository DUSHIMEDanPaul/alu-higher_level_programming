#!/usr/bin/python3

def add_integer(a, b=98):
    """
    This function adds two integers.
    
    >>> add_integer(3, 98)
    101
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()




