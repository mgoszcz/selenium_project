
from typing import List

VOWELS = ('a', 'e', 'i', 'o', 'u')


def pick_out_vowels(text_string: str) -> List[str]:
    """Returns list of vowels from input string"""
    result = []
    if not isinstance(text_string, str):
        raise TypeError('Input argument must be a string')
    for letter in text_string:
        if letter.lower() in VOWELS:
            result.append(letter)
    return result
