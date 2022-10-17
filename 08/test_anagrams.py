import unittest

from anagrams import find_anagrams


class TestAnagrams(unittest.TestCase):
    """
    This class tests anagams module.
    """

    def test_find_anagrams_empties(self):
        actual = find_anagrams('', '')
        self.assertEqual(actual, [])

        actual = find_anagrams('', 'abc')
        self.assertEqual(actual, [])

        actual = find_anagrams('cba', '')
        self.assertEqual(actual, [])

    def test_find_anagrams(self):
        actual = find_anagrams('cartreecboyRacarcarca', 'car')
        self.assertEqual(actual, [0, 13, 14, 15, 16, 17, 18])

        actual = find_anagrams('cArtreeboyRacarCarca', 'car')
        self.assertEqual(actual, [12, 16, 17])

        actual = find_anagrams('ca', 'car')
        self.assertEqual(actual, [])

        actual = find_anagrams('CaRcAr', 'cAr')
        self.assertEqual(actual, [3])

        actual = find_anagrams('qwqw', 'qw')
        self.assertEqual(actual, [0, 1, 2])
