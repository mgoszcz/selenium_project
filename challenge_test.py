from unittest import TestCase

from Challenge import pick_out_vowels

TEST_DATA_POSITIVE = {
    'Hello, today is Monday': ['e', 'o', 'o', 'a', 'i', 'o', 'a'],
    'I AM MARCIN': ['I', 'A', 'A', 'I'],
    'T u e s d a y': ['u', 'e', 'a']
}

TEST_DATA_NEGATIVE = ['1234567890', '!@#$^%&*(^)(&']
TEST_DATA_NEGATIVE_EXPECTED_VALUE = []
TEST_DATA_EXCEPTION = [1, 2.5, (), {}, []]


class ChallengeTest(TestCase):

    def test_challenge_positive(self):
        for string_to_test, expected_result in TEST_DATA_POSITIVE.items():
            self.assertEqual(expected_result, pick_out_vowels(string_to_test), f'String under test: {string_to_test}')

    def test_challenge_negative(self):
        for string_to_test in TEST_DATA_NEGATIVE:
            self.assertEqual(TEST_DATA_NEGATIVE_EXPECTED_VALUE, pick_out_vowels(string_to_test),
                             f'String under test: {string_to_test}')

    def test_challenge_exception(self):
        for variable_to_test in TEST_DATA_EXCEPTION:
            with self.assertRaises(TypeError,
                                   msg=f'Variable under test: {variable_to_test}, type: {type(variable_to_test)}'):
                pick_out_vowels(variable_to_test)
