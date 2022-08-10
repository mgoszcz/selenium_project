"""Module contains ChallengeTest class"""
from unittest import TestCase

from .challenge import pick_out_vowels

TEST_DATA_POSITIVE = {
    'Hello, today is Monday': ['e', 'o', 'o', 'a', 'i', 'o', 'a'],
    'I AM MARCIN': ['I', 'A', 'A', 'I'],
    'T u e s d a y': ['u', 'e', 'a']
}

TEST_DATA_NEGATIVE = ['1234567890', '!@#$^%&*(^)(&']
TEST_DATA_NEGATIVE_EXPECTED_VALUE = []
TEST_DATA_EXCEPTION = [1, 2.5, (), {}, []]


class ChallengeTest(TestCase):
    """Class contains all test cases for testing pick_out_vowels method"""

    def test_challenge_positive(self):
        """Verify positive scenarios - correct string as an input should give expected list of characters"""
        for string_to_test, expected_result in TEST_DATA_POSITIVE.items():
            self.assertEqual(expected_result, pick_out_vowels(string_to_test), f'String under test: {string_to_test}')

    def test_challenge_negative(self):
        """Verify negative scenario - strings without letters should return empty list"""
        for string_to_test in TEST_DATA_NEGATIVE:
            self.assertEqual(TEST_DATA_NEGATIVE_EXPECTED_VALUE, pick_out_vowels(string_to_test),
                             f'String under test: {string_to_test}')

    def test_challenge_exception(self):
        """
        Verify negative scenario - error handling - function should raise type error when wrong type of input provided
        """
        for variable_to_test in TEST_DATA_EXCEPTION:
            with self.assertRaises(TypeError,
                                   msg=f'Variable under test: {variable_to_test}, type: {type(variable_to_test)}'):
                pick_out_vowels(variable_to_test)
