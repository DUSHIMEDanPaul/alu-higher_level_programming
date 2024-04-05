def say_my_name(first_name, last_name=""):
    """
    the following function takes two names though it will rejects arguments that are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)


