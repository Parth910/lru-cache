from .node import Node
from .exceptions import CapacityError

#class LRUCache
class LRUCache:
    #LRUCache constructor
    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("Cache capacity cannot be negative")
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    #remove node from cache
    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
    #add node to cache
    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    #get value from cache
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    #put value in cache
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            raise CapacityError("Cache capacity must be greater than 0")
            
        if key in self.cache:
            self._remove(self.cache[key])
            del self.cache[key]
            
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)
        
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]
            
            
            
            
        