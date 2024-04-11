#!/usr/bin/python3
def text_indentation(text):
    """
    Add two new lines after each '.', '?' and ':' in the text.
    Remove spaces at the beginning or end of each printed line.
    """
    ...


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    special_chars = ['.', '?', ':']
    for char in special_chars:
        text = text.replace(char, char + '\n\n')
    
    lines = text.split('\n')
    lines = [line.strip() for line in lines]
    text = '\n'.join(lines)
    
    print(text)

