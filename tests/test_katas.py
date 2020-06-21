import unittest
import katas
import importlib
import sys
import inspect
import random

target = __import__('katas')

class TestKatas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # This will import the module to be tested
        cls.module = importlib.import_module('katas')
        # make a dictionary of each function in the test module
        cls.funcs = {
            k: v for k, v in inspect.getmembers(
                cls.module, inspect.isfunction
                )
            }
        # check the funcs for required functions
        assert "add" in cls.funcs, "Missing the add() function"
        assert "multiply" in cls.funcs, "Missing the multiply() function"
        assert "power" in cls.funcs, "Missing the power() function"
        assert "factorial" in cls.funcs, "Missing the factorial() function"
        assert "fibonacci" in cls.funcs, "Missing the fibonacci() function"

    def test_add(self):
        add = self.module.add
        self.assertEqual(add(5, 10), 15, "Should be 15")
        self.assertEqual(add(9, 21), 30, "Should be 30")
        # self.fail("TODO: Write add unit test")

    def test_multiply(self):
        add = self.module.add
        multiply = self.module.multiply
        self.assertEqual(multiply(3, 2), 6, "Should equal 6")
        self.assertEqual(multiply(5, 10), 50, "Should equal 50")
        self.assertEqual(multiply(add(3, 3), add(4, 2)), 36, "Should equal 36")

        # self.fail("TODO: Write multiply unit test")

    def test_power(self):
        power = self.module.power
        self.assertEqual(power(3, 2), 9, "Should equal 9")
        # self.fail("TODO: Write power unit test")

    def test_factorial(self):
        fact = self.module.factorial
        self.assertEqual(fact(5), 120, "Should equal 120")
        self.assertEqual(fact(9), 362880, "Should be 362880")

        # self.fail("TODO: Write factorial unit test")

    def test_fibonacci(self):
        fib = self.module.fibonacci
        self.assertEqual(fib(7), 8)
        self.assertEqual(fib(14), 233)
        self.assertEqual(fib(18), 1597)
        # self.fail("TODO: Write fibonacci unit test")


if __name__ == '__main__':
    unittest.main()
