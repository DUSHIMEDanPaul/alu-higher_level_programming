#!/usr/bin/python3
"""
This module contains a function called say_my_name. The function takes two parameters: 
first_name and last_name. It prints a greeting using these names. If no last_name is 
provided, it defaults to an empty string. The function raises a TypeError if either 
first_name or last_name is not a string.

Example:
    >>> from module_name import say_my_name
    >>> say_my_name("John", "Doe")
    My name is John Doe
"""


def say_my_name(first_name, last_name=""):
    """
    the following function takes two names though it will rejects arguments that are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

