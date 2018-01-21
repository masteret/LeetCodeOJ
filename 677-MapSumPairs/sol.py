class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.data[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        result = 0
        for key in self.data.keys():
            if key.startswith(prefix):
                result += self.data[key]
        return result


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)