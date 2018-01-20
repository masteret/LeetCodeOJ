class Solution(object):
    def isPrime(self, n):
        if n in [2,3,5,7]:
            return True
        if n == 1 or n % 2 == 0 or n % 3 == 0:
            return False
        tmp = int(n**0.5)
        for x in range(2, tmp+1):
            if n % x == 0:
                return False
        return True

    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        for x in range(L, R+1):
            tmp = "{0:b}".format(x).count("1")
            if self.isPrime(tmp):
                count += 1
        return count

a = Solution()
print a.isPrime(37)
print a.countPrimeSetBits(6, 10)