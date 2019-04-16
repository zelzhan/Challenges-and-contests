from collections import OrderedDict
import sys
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hashtable = OrderedDict()
        self.capacity = capacity
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hashtable:
            return -1
        else:
            value = self.hashtable[key]
            del self.hashtable[key]
            self.hashtable[key] = value
        
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashtable:
            del self.hashtable[key]
        self.hashtable[key] = value
        if len(self.hashtable) > self.capacity:
            self.hashtable.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
