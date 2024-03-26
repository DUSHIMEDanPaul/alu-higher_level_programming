#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function adds two integers.

    Args:
    a: The first integer or float to add. Must be convertible to an integer.
    b: The second integer or float to add. Must be convertible to an integer. Defaults to 98.

    Returns:
    The sum of a and b, as an integer.

    Doctest:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100)
    198
    >>> add_integer(1.5, 2.5)
    3
    >>> add_integer(-1, -2)
    -3
    >>> add_integer('a', 1)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    >>> add_integer(1, 'b')
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer
    >>> add_integer('a', 'b')
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)



