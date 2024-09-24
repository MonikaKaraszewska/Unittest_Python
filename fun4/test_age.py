from age import categorize_by_age

import unittest

class TestCategorizeByAge(unittest.TestCase):


    def test_child(self):
        '''Test for child'''
        for number in [0,1,2,3,4,5,6,7,8,9]:
            with self.subTest(number=number):
                self.assertEqual(categorize_by_age(number),"Child")

    def test_adult(self):
        '''Test for adult'''
        for k in [19,20,50,65]:
            with self.subTest(number=k):
                self.assertEqual(categorize_by_age(k), "Adult")

    def test_floats(self):
        self.assertEqual(categorize_by_age(7.5), "Child")

    def test_adolescence(self):
        '''test to adolescence'''
        for number in [10,11,15,17,18]:
            with self.subTest(number=number):
                self.assertEqual(categorize_by_age(number), "Adolescent")

    def test_negative_number(self):
        age = -7
        self.assertEqual(categorize_by_age(age), f"Invalid age: {age}")

    def test_boundary(self):
        self.assertEqual(categorize_by_age(9), "Child")
        self.assertEqual(categorize_by_age(10), "Adolescent")
        self.assertEqual(categorize_by_age(19), "Adult")
        self.assertEqual(categorize_by_age(18), "Adolescent")

    @unittest.skip("einfach so")
    def test_to_old(self):
        self.assertEqual(categorize_by_age(151), f"Invalid age: 11")

if __name__ == '__main__':
    unittest.main(verbosity=2)