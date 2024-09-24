import unittest

from czy_rowne import czy_sa_rowne

class TestCzRowne(unittest.TestCase):


    def test_True(self):
        print(f"module name z inn: {__name__}")
        # Expect the first and last elements (30 and 30) to be equal, so it should return True
        self.assertTrue(czy_sa_rowne([30, 65, 35, 75, 30]), 'First and last elements should be equal')

    def test_False(self):
        # Expect the first and last elements (30 and 40) to be unequal, so it should return False
        self.assertFalse(czy_sa_rowne([30, 65, 35, 75, 40]), 'First and last elements should not be equal')

    def test_both_str_numeric_notEqual(self):
        self.assertFalse(czy_sa_rowne(['30', 65, 35, 75, '40']),
                        'First and last elements are numeric strings and should NOT be equal')


    def test_both_str_numeric_Equal(self):
        self.assertTrue(czy_sa_rowne(['30', 65, 35, 75, '30']),
                        'First and last elements are numeric strings and should be equal')

    def test_str_numeric(self):
        # Even though '30' is a string, it should be converted to an integer and compared to 30
        self.assertTrue(czy_sa_rowne(['30', 65, 35, 75, 30]),
                        'First and last elements are numeric and should be equal, even if one is a string')

    def test_str_alpha(self):
        # 'liczba' is a non-numeric string, so the function should return False
        self.assertFalse(czy_sa_rowne(['liczba', 65, 35, 75, 30]),
                         'First element is a non-numeric string, so it should return False')


if __name__ == '__main__':
    unittest.main()


