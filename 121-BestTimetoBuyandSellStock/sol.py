class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_min = float('inf')
        max_profit = 0
        for x in prices:
            cur_min = min(cur_min, x)
            profit = x-cur_min
            max_profit = max(profit, max_profit)
        return max_profit

a = Solution()
print a.maxProfit([7,1,5,3,6,4])
print a.maxProfit([7, 6, 4, 3, 1])