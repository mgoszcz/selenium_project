"""Test suite for testing pick_out_vowels function"""
import unittest

from vowels_test.challenge_test import ChallengeTest

suite = unittest.defaultTestLoader.loadTestsFromTestCase(ChallengeTest)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(f'Tests Run: {result.testsRun}, Errors: {len(result.errors)}, Failures: {len(result.failures)}')