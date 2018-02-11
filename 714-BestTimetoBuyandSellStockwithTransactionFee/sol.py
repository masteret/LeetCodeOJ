class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108867/C++-concise-solution-O(n)-time-O(1)-space
        sell_profit = 0
        buy_profit = -2**31+1
        for x in prices:
            tmp = sell_profit
            sell_profit = max(sell_profit, buy_profit+x-fee)
            buy_profit = max(buy_profit, tmp-x-fee)
        return sell_profit