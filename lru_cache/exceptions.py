class LRUCacheException(Exception):
    """Base class for all LRUCache exceptions"""
    pass

class CapacityError(LRUCacheException):
    """Exception raised when the cache capacity is exceeded"""
    