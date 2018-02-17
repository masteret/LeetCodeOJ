class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0]*(len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for x in range(2, len(dp)):
            dp[x] = cost[x]+min(dp[x-1], dp[x-2])
        return min(dp[-1], dp[-2])

a = Solution()
print a.minCostClimbingStairs([10, 15, 20])
print a.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])