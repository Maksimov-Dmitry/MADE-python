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
        actual = find_anagrams('car tree c boy Rac  arc arca', 'car')
        self.assertEqual(actual, [0, 5])

        actual = find_anagrams('cAr tree boy Rac arC arca', 'car')
        self.assertEqual(actual, [])
