import unittest

from silnia import factorial

class TestSilnia(unittest.TestCase):
    def setUp(self):
        print('set up - powienien pojawiac sie przed kazdym testem,kazda funkcja')

    def test_jeden(self):
        '''test jeden = jeden'''
        self.assertEqual(1,1)
        print('test_jeden sie wykonuje')


    def test_4(self):
        '''test dla 4,ma byc 24'''
        self.assertEqual(factorial(4),24)
        print('test_4 sie wykonuje')

    def test_ujemnych(self):
        '''test dla ujemnych'''
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_zero(self):
        '''test zero = jeden'''
        self.assertEqual(factorial(0), 1)

    def tearDown(self):
        print('a to  po zakonczeniu testu')

if __name__ == '__main':
    unittest.main()