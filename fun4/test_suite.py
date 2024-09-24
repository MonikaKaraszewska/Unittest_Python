import unittest
from test_jak import TestIsPrime
from test_age import TestCategorizeByAge

def make_suite_1():
    age_tests = [
        TestCategorizeByAge('test_child'),
        TestCategorizeByAge('test_adolescence'),
        TestCategorizeByAge('test_adult'),
        TestIsPrime('test_prime_number')
    ]


    return unittest.TestSuite(tests=age_tests), unittest

def suite_numbers():
    numbers_tests = [
        TestCategorizeByAge('test_floats'),
        TestCategorizeByAge('test_negative_number'),
        TestIsPrime('test_negative_number'),
        TestIsPrime('test_zero_and_one')
    ]
    return unittest.TestSuite(tests=numbers_tests)



if __name__ == '__main__':
    suite = make_suite_1()
    suite2 = suite_numbers()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    runner.run(suite2)