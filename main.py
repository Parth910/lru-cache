from lru_cache.cache import LRUCache
from lru_cache.exceptions import CapacityError

try:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # Output: 1
    print(cache.get(2))  # Output: 2
    cache.put(3, 3)
    print(cache.get(2))  # Output: -1
    print(cache.get(3))  # Output: 3
    cache.put(4, 4)
    print(cache.get(1))  # Output: -1
    print(cache.get(3))  # Output: 3
    print(cache.get(4))  # Output: 4
except CapacityError as e:
    print(e)