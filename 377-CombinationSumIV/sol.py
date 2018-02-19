class Solution(object):
    def helper(self, nums, target):
        if target in self.result:
            return self.result[target]

        result = 0
        for x in range(len(nums)):
            if target-nums[x] >= 0:
                result += self.helper(nums, target-nums[x])
        self.result[target] = result
        return result

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.result = {0: 1}
        self.helper(nums, target)
        return self.result[target]

a = Solution()
print a.combinationSum4([1,2,3], 4)
print a.combinationSum4([1,2,4], 32)
print a.combinationSum4([3,1,2,4], 4)