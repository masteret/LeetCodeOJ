class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.used_count = {}
        self.recent = []
        self.capacity = capacity

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print "cache: ", result.cache, " used count: ", result.used_count, " recent: ", result.recent
        return wrapper

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if str(key) in self.cache:
            # increase used count

            # move to recent
            return self.cache[str(key)]
        else:
            return -1            

    @decorator
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # insert to cache
        self.cache[str(key)] = value
        # increased used count
        self.used_count[str(key)] = self.used_count[str(key)] + 1 if str(key) in self.used_count else 1
        # move to recent
        # pop itself
        if key in self.recent:
            self.recent.pop(self.recent.index(key))
            self.recent.append(key)
        # pop others
        elif len(self.recent) == self.capacity:
            poped = self.recent.pop(0)
            del self.cache[str(poped)]
            del self.used_count[str(poped)]
            self.recent.append(key)
        # no need to pop
        else:
            self.recent.append(key)
        # invalidate least use cache
            # self.cache
            # used count
        return self


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