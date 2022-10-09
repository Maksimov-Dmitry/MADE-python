import unittest

from lru_cache import LRUCache


class TestTicTacGame(unittest.TestCase):
    """
    This class tests LRUCache class.
    """

    def test_wrong_init(self):
        with self.assertRaises(ValueError) as context:
            LRUCache(2.2)
        self.assertEqual(str(context.exception),
                         'Limit must be integer and >= 1, was 2.2.')

        with self.assertRaises(ValueError) as context:
            LRUCache(0)
        self.assertEqual(str(context.exception),
                         'Limit must be integer and >= 1, was 0.')

    def test_set_and_get(self):
        lru_cache = LRUCache(2)

        lru_cache.set('k1', 'val1')
        self.assertDictEqual(lru_cache.data, {'k1': 'val1'})

        lru_cache.set('k2', 'val2')
        self.assertDictEqual(lru_cache.data, {'k1': 'val1', 'k2': 'val2'})
        self.assertListEqual(list(lru_cache.data.keys()), ['k1', 'k2'])

        val = lru_cache.get('k3')
        self.assertIsNone(val)
        self.assertDictEqual(lru_cache.data, {'k1': 'val1', 'k2': 'val2'})
        self.assertListEqual(list(lru_cache.data.keys()), ['k1', 'k2'])

        val = lru_cache.get('k2')
        self.assertEqual(val, 'val2')
        self.assertDictEqual(lru_cache.data, {'k1': 'val1', 'k2': 'val2'})
        self.assertListEqual(list(lru_cache.data.keys()), ['k1', 'k2'])

        val = lru_cache.get('k1')
        self.assertEqual(val, 'val1')
        self.assertDictEqual(lru_cache.data, {'k2': 'val2', 'k1': 'val1'})
        self.assertListEqual(list(lru_cache.data.keys()), ['k2', 'k1'])

        lru_cache.set('k3', 'val3')
        self.assertDictEqual(lru_cache.data, {'k1': 'val1', 'k3': 'val3'})
        self.assertListEqual(list(lru_cache.data.keys()), ['k1', 'k3'])

        val = lru_cache.get('k3')
        self.assertEqual(val, 'val3')
        self.assertDictEqual(lru_cache.data, {'k1': 'val1', 'k3': 'val3'})
        self.assertListEqual(list(lru_cache.data.keys()), ['k1', 'k3'])

        val = lru_cache.get('k2')
        self.assertIsNone(val)
        self.assertDictEqual(lru_cache.data, {'k1': 'val1', 'k3': 'val3'})
        self.assertListEqual(list(lru_cache.data.keys()), ['k1', 'k3'])

        val = lru_cache.get('k1')
        self.assertEqual(val, 'val1')
        self.assertEqual(lru_cache.data, {'k3': 'val3', 'k1': 'val1'})
        self.assertListEqual(list(lru_cache.data.keys()), ['k3', 'k1'])

        lru_cache.set('k3', 'val_3_1')
        self.assertEqual(lru_cache.data, {'k1': 'val1', 'k3': 'val_3_1'})
        self.assertListEqual(list(lru_cache.data.keys()), ['k1', 'k3'])

        lru_cache.set('k3', 'val_3_2')
        self.assertEqual(lru_cache.data, {'k1': 'val1', 'k3': 'val_3_2'})
        self.assertListEqual(list(lru_cache.data.keys()), ['k1', 'k3'])
