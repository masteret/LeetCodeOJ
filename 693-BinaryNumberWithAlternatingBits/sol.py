class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        string = "{0:b}".format(n)
        if "00" in string or "11" in string:
            return False
        return True