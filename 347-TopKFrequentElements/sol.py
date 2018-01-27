class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for x in nums:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1

        result = sorted(count.keys(), key=count.get, reverse=True)[:k]
        return result