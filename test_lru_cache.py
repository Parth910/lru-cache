import unittest
from lru_cache.cache import LRUCache
from lru_cache.exceptions import CapacityError
class TestLRUCache(unittest.TestCase):
    def test_basic_operations(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)  # Should evict key 2
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)

    def test_zero_capacity(self):
        cache = LRUCache(0)
        with self.assertRaises(CapacityError):  
            cache.put(1, 1)

    def test_negative_capacity(self):
        with self.assertRaises(ValueError):
            LRUCache(-1)

    def test_duplicate_keys(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(1, 2)  # Update existing key
        self.assertEqual(cache.get(1), 2)

    def test_nonexistent_key(self):
        cache = LRUCache(2)
        self.assertEqual(cache.get(1), -1)

    def test_full_capacity_operations(self):
        cache = LRUCache(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        cache.put(4, 4)  # Should evict key 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_lru_order(self):
        cache = LRUCache(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        cache.get(1)  # Move 1 to front
        cache.put(4, 4)  # Should evict key 2
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(1, 3)  # Update key 1
        cache.put(3, 3)  # Should evict key 2
        self.assertEqual(cache.get(1), 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)

    def test_large_capacity(self):
        cache = LRUCache(1000)
        for i in range(1000):
            cache.put(i, i)
        for i in range(1000):
            self.assertEqual(cache.get(i), i)

if __name__ == '__main__':
    unittest.main()