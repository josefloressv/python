"""
This is a simple example of how to use the unittest module in Python.
The unittest module provides a rich set of tools for constructing and running tests.
Each test case is a class that inherits from unittest.TestCase.
The test methods should start with the word test.
"""
import unittest

class ExampleTest(unittest.TestCase):
    def test_sum_two_numbers(self):
        number1 = 10
        number2 = 20

        result = number1 + number2
        self.assertEqual(result, 30)

    def test_rest_two_numbers(self):
        number1 = 10
        number2 = 20

        result = number1 - number2
        self.assertEqual(result, -10)

if __name__ == "__main__":
    unittest.main() # this will run the all the tests