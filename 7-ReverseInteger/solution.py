class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import sys
        if x < 0:
            answer = int("-"+str(x)[::-1][:-1])
        else:
            answer = int(str(x)[::-1])

        if answer > pow(2,31) or answer < -pow(2,31)-1:
            return 0
        return answer

a = Solution()
print a.reverse(123)
print a.reverse(-123)
print a.reverse(1534236469)