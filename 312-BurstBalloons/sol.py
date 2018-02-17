class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for x in range(n)] for y in range(n)]

        def cal(i, j):
            if dp[i][j] or i+1 == j:
                return dp[i][j]
            val = 0
            for x in range(i+1, j):
                val = max(val, nums[i]*nums[x]*nums[j]+cal(i,x)+cal(x,j))
            dp[i][j] = val
            return dp[i][j]
        return cal(0, n-1)