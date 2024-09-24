import unittest

from palindrom import is_palindrome

class test_palindrome(unittest.TestCase):

    def test_pusty_string(self):
        '''pusty string'''
        self.assertTrue(is_palindrome(''))


    def test_sentences(self):
        '''rozne zdania'''
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
        self.assertFalse(is_palindrome('kto to'))
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))

    def test_multi_words(self):
        '''set fo words'''
        for word in ['radar', 'level', 'civic']:
            with self.subTest(s=word):
                self.assertTrue(is_palindrome(word))

    def test_numbers(self):
        self.assertTrue(is_palindrome('121'))


if __name__ == '__main__':
    unittest.main()