# This task is based on Array and String manipulation.
#
# You need to set up a simple project in the given programming language and create 2 files and give them some meaningful names eg:
#
# Challenge.java (.js .py etc as applicable) - the coding solution
# ChallengeTest.java (.js .py etc) - unit tests for the solution
# Your task is to create the following method and unit tests for it. Your project should build and run successfully and all unit tests should pass.
#
# Task Breakdown
#
# Sample input is a string "Hello, today is Monday".
#
# pickOutVowels method - this method should take in any sentence and return an array of vowels included in the sentence, in the same order they occur in it. Example:
# 1pickOutVowels('Hello, today is Monday');
#
# 2// returns ['e', 'o', 'o', 'a', 'i', 'o', 'a']
from typing import List

VOWELS = ('a', 'e', 'i', 'o', 'u')


def pick_out_vowels(text_string: str) -> List[str]:
    result = []
    if type(text_string) != str:
        raise TypeError('Input argument must be a string')
    for letter in text_string:
        if letter.lower() in VOWELS:
            result.append(letter)
    return result

print(pick_out_vowels('Hello, today is Monday'))
