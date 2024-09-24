import unittest

from age_exceptions import categorize_by_age_except

class test_excetions(unittest.TestCase):

    def test_age_str(self):
        with self.assertRaises(TypeError):
            categorize_by_age_except('h')
        with self.assertRaises(TypeError):
            categorize_by_age_except()