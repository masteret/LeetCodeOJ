class Solution(object):
    def isPrime(self, n):
        for x in range(2, int(n**0.5+1)):
            if n%x == 0:
                return x
        return -1

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = {
            1:0,
            2:2,
            3:3
        }
        for x in range(4, n+1):
            tmp = self.isPrime(x)
            if tmp == -1:
                result[x] = x
            else:
                result[x] = result[tmp] + result[x/tmp]
        return result[n]