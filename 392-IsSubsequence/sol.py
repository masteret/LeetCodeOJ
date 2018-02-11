class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for x in s:
            ind = t.find(x)
            if ind != -1:
                t = t[ind+1:]
            else:
                return False
        return True