# Virginia Link
# 02/25/2021
# Inclass Activity 3

import unittest

import fib

class Test(unittest.TestCase):
    def test_good_input(self):
        result = fib.fib(5)
        self.assertEqual(result, 3)
    def test_zero_input(self):
        result = fib.fib(0)
        self.assertEqual(result,0)



if __name__ == '__main__':
    unittest.main()

