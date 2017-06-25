class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        for x in range(num+1):
            result.append((bin(x)[2:].count("1")))
        return result

a = Solution()
print a.countBits(5)