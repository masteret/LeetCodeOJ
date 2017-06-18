class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:]
        y = bin(y)[2:]
        x = x[::-1].ljust(max(len(x), len(y)), "0")
        y = y[::-1].ljust(max(len(x), len(y)), "0")
        return len([True for ind in range(len(x)) if (x[ind] != y[ind])])

a = Solution()
print a.hammingDistance(1, 4)