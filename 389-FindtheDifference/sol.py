class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum1 = 0
        sum2 = 0
        for x in s:
            sum1 += ord(x)
        for x in t:
            sum2 += ord(x)
        return chr(abs(sum1-sum2))