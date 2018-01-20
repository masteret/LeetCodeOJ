class Solution(object):
    def isPalindrom(self, s):
        if len(s) % 2 == 0:
            first = s[:(len(s)/2)]
            second = s[(len(s)/2):]
            return first == second[::-1]
        else:
            first = s[:(len(s)/2)]
            second = s[(len(s)/2)+1:]
            return first == second[::-1]

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = len(s)
        for x in range(2,len(s)+1):
            for y in range(len(s)-x+1):
                string = s[y:y+x]
                if self.isPalindrom(string):
                    count += 1
        return count

a = Solution()
print a.countSubstrings("abc")
print a.countSubstrings("aaa")