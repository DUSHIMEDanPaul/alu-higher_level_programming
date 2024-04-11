#!/usr/bin/python3
"""Define text-identation function Below."""

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

