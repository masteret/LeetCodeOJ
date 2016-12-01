import collections

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.used_count = {}
        self.recent = []
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if str(key) in self.cache:
            # increase used count
            self.used_count[str(key)] += 1
            # move to recent
            self.recent.pop(self.recent.index(key))
            self.recent.append(key)

            return self.cache[str(key)]
        else:
            return -1            

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return None

        # invalidate least use cache
        if len(self.recent) == self.capacity and key not in self.recent:
            sorted_used_count = collections.Counter(self.used_count).most_common()[::-1]
            # find the least 
            least_commons = [k for k, v in sorted_used_count if v == sorted_used_count[0][1]]
            least_recent = min([self.recent.index(int(x)) for x in least_commons if int(x) in self.recent])
            poped = str(self.recent[least_recent])

            del self.cache[poped]
            del self.used_count[poped]
            self.recent.pop(self.recent.index(int(poped)))

        # insert to cache
        self.cache[str(key)] = value
        # increased used count
        self.used_count[str(key)] = self.used_count[str(key)] + 1 if str(key) in self.used_count else 1
        # move to recent
        # pop itself
        if key in self.recent:
            self.recent.pop(self.recent.index(key))
            self.recent.append(key)
        # no need to pop
        else:
            self.recent.append(key)

# obj = LFUCache(2)
# obj.set(1, 1)
# obj.set(2, 2)
# print obj.get(1)
# obj.set(3, 3)
# print obj.get(2)
# print obj.get(3) 
# obj.set(4, 4) 
# print obj.get(1)
# print obj.get(3)
# print obj.get(4) 

# obj = LFUCache(0)
# obj.set(0, 0)
# print obj.get(0)

obj = LFUCache(2)
print obj.get(2)
print obj.set(2,6)
print obj.get(1)
print obj.set(1,5)
print obj.set(1,2)
print obj.get(1)
print obj.get(2)