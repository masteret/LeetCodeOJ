class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for x in range(len(prices)-1):
            if prices[x] < prices[x+1]:
                result += prices[x+1] - prices[x]
        return result