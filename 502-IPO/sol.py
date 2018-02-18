class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        import heapq
        heap = []
        pair = zip(Capital, Profits)
        pair = sorted(pair, key=lambda x: x[0])
        cur = 0
        for x in range(k):
            while cur < len(pair) and W >= pair[cur][0]:
                heapq.heappush(heap, -pair[cur][1])
                cur += 1
            if heap:
                W -= heapq.heappop(heap)
        return W

a = Solution()
print a.findMaximizedCapital(2, 0, [1,2,3], [0,1,1])