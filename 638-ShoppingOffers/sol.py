class Solution(object):
    def justBuy(self, price, needs):
        total = 0
        for ind in range(len(needs)):
            total += price[ind]*needs[ind]
        return total

    def verify(self, deal, needs):
        return all([needs[x]-deal[x] >= 0 for x in range(len(needs))])

    def findmin(self, price, special, needs):
        result = self.justBuy(price, needs)
        for deal in special:
            if self.verify(deal, needs):
                result = min(result, deal[-1]+self.findmin(price, special, [needs[x]-deal[x] for x in range(len(needs))]))
        return result

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        return self.findmin(price, special, needs)