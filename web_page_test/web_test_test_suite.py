"""Test suite for testing web application"""
import unittest

from web_page_test.test_cases.web_test_negative_tests import WebTestNegativeTests
from web_page_test.test_cases.web_test_positive_tests import WebTestPositiveTests

suite = unittest.defaultTestLoader.loadTestsFromTestCase(WebTestNegativeTests)
suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(WebTestPositiveTests))


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    print(f'Tests Run: {result.testsRun}, Errors: {len(result.errors)}, Failures: {len(result.failures)}')