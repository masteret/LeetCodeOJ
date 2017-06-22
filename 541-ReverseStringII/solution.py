class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) <= k:
            return s[::-1]
        elif len(s) <= 2*k:
            return s[:k][::-1] + s[k:]
        else:
            result = ""
            for x in range(0, len(s), 2*k):
                result = result + s[x:x+k][::-1] + s[x+k:x+2*k]
            return result

a = Solution()
print a.reverseStr("abcdefg", 2)
print a.reverseStr("abcd", 2)