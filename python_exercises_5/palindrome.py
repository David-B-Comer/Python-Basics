"""
This function determines if a word or phrase is a palindrome
:param value: A string
:return: A boolean
"""

import string

def remove_punctuations(value):
    return "".join(i.lower() for i in value if i in string.ascii_letters)

def reverse(value):
    return value[::-1]

def is_palindrome(value: str) -> bool:
    value = remove_punctuations(value)
    return value==reverse(value)