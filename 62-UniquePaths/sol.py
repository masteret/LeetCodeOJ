class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for x in range(n)] for y in range(m)]
        for x in range(n):
            dp[m-1][x] = 1
        for x in range(m):
            dp[x][n-1] = 1
        for x in range(m-2, -1, -1):
            for y in range(n-2, -1, -1):
                dp[x][y] = dp[x+1][y] + dp[x][y+1]
        for x in dp:
            print x
        return dp[0][0]

a = Solution()
print a.uniquePaths(20, 20)