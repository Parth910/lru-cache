# LRU Cache Implementation

A Python implementation of a Least Recently Used (LRU) Cache data structure.

## Dependencies

- Python 3.6 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Parth910/lru-cache.git
cd lru-cache
```

2. Run the example implementation:
   ```bash
   python main.py
   ```
   This will demonstrate the LRU cache operations with the following sequence:
   - Initialize cache with capacity 2
   - Put key-value pairs (1,1) and (2,2)
   - Get values for keys 1 and 2
   - Put key-value pair (3,3), which evicts key 1
   - Get values for keys 2 and 3
   - Put key-value pair (4,4), which evicts key 2
   - Get values for keys 1, 3, and 4

## Features

- Fixed-size cache with configurable capacity
- O(1) time complexity for both get and put operations
- Automatic eviction of least recently used items when capacity is reached
- Thread-safe implementation
- Comprehensive test coverage

## Usage

```python
from lru_cache.cache import LRUCache
from lru_cache.exceptions import CapacityError

# Create a cache with capacity of 2
cache = LRUCache(2)

# Add items to cache
cache.put(1, 1)
cache.put(2, 2)

# Retrieve items
print(cache.get(1))  # Returns 1
print(cache.get(2))  # Returns 2

# When cache is full, least recently used item is evicted
cache.put(3, 3)      # Evicts key 1
print(cache.get(1))  # Returns -1 (not found)
print(cache.get(3))  # Returns 3
```

## API Reference

### LRUCache(capacity: int)

Creates a new LRU cache with the specified capacity.

- `capacity`: Maximum number of items the cache can hold
- Raises `ValueError` if capacity is negative
- Raises `CapacityError` if capacity is zero

### Methods

#### get(key: int) -> int

Retrieves the value for the given key.

- Returns the value if key exists
- Returns -1 if key doesn't exist
- Time complexity: O(1)

#### put(key: int, value: int) -> None

Adds or updates a key-value pair in the cache.

- If key exists, updates its value
- If key doesn't exist, adds new key-value pair
- If cache is full, evicts least recently used item
- Time complexity: O(1)

## Running Tests

To run the test suite:

```bash
python3 -m unittest test_lru_cache.py
```

## Implementation Details

The LRU Cache is implemented using a combination of:
- Doubly linked list for O(1) insertion and deletion
- Hash map for O(1) lookups
