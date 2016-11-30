class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.used_count = {}
        self.recent = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if str(key) in self.cache:
            return self.cache[str(key)]
        else:
            return -1            

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.cache[str(key)] = value


# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(2)
# param_1 = obj.get(key)
# obj.set(key,value)

obj.set(1, 1)
obj.set(2, 2)
print obj.get(1)
obj.set(3, 3)
print obj.get(2)
print obj.get(3) 
obj.set(4, 4) 
print obj.get(1)
print obj.get(3)
print obj.get(4) 