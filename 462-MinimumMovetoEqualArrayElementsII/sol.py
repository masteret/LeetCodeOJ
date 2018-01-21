class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from statistics import median
        mid = median(nums)
        result = 0
        for x in nums:
            result += abs(mid-x)
        return int(result)