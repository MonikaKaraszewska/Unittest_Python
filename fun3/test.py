import unittest
from text_fun import analyze_text

text1 = 'Powodzenia w pisaniu testów! Jeśli potrzebujesz wskazówek dotyczących konkretnych testów, daj znać.'


class test_analyze_text(unittest.TestCase):

    def test_happy_path(self):
        self.assertDictEqual(analyze_text(text1),{'length': 99, 'words': 12, 'uppercase': 2,
                                                  'lowercase': 83, 'digits': 0, 'spaces': 11, 'most_common': ' '}, "checks text")

    def test_key_in(self):
        result = analyze_text(text1)
        self.assertIn('words', result)

    def test_is_dict(self):
        self.assertIsInstance(analyze_text(text1), dict)

    def test_number_keys(self):
        dlugosc = len(analyze_text(text1))
        self.assertEqual(dlugosc, 7)
