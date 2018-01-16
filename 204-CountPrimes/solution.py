class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        a = [True]*(n-1)
        for x in range(2, int(sqrt(n))+1):
            if a[x-1]:
                for y in range(x*x, n, x):
                    a[y-1] = False
        count = 0
        for x in a:
            if x:
                count += 1
        return count-1 if count > 0 else 0

a = Solution()
print a.countPrimes(52)