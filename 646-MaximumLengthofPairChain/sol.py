class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda x: x[1])
        cur = pairs[0]
        count = 1
        for pair in pairs:
            if cur[1] < pair[0]:
                cur = pair
                count += 1
        return count