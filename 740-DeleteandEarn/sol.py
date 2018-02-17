class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = [0]*10001
        for x in nums:
            total[x] += x

        last_skip = 0
        last_take = 0
        for v in total:
            skip = max(last_skip, last_take)
            take = last_skip+v
            last_skip = skip
            last_take = take

        return max(last_skip, last_take)