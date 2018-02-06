class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # result = {}
        # result[1] = 1
        # result[2] = 1
        # result[3] = 2
        # for x in range(4, n+1):
        #     tmp = range(x-1, x/2-1, -1)
        #     scan = set((a, x-a) for a in tmp)
        #     scan.update(set((result[a], result[x-a]) for a in tmp))
        #     scan.update(set((a, result[x-a]) for a in tmp))
        #     scan.update(set((result[a], x-a) for a in tmp))
        #     result[x] = max([a*b for a, b in scan])
        # return result[n]
        if n == 2:
            return 1
        if n == 3:
            return 2
        result = 1
        while (n > 4):
            result *= 3
            n -= 3
        result *= n
        return result

a = Solution()
print a.integerBreak(2)
print a.integerBreak(8)
print a.integerBreak(10)