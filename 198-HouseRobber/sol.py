class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_skip = 0
        last_take = 0
        for v in nums:
            skip = max(last_skip, last_take)
            take = last_skip+v
            last_skip = skip
            last_take = take

        return max(last_skip, last_take)