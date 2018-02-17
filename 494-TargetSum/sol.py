class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        result = {nums[0]:1, -nums[0]:1} if nums[0] != 0 else {0:2}
        for i in range(1, len(nums)):
            tmp = {}
            for k in result:
                tmp[k+nums[i]] = tmp.get(k+nums[i], 0) + result.get(k, 0)
                tmp[k-nums[i]] = tmp.get(k-nums[i], 0) + result.get(k, 0)
            result = tmp
        return result.get(S, 0)