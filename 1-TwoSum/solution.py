class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return False
        reference = {}
        for x in range(len(nums)):
            if nums[x] in reference:
                return [reference[nums[x]], x]
            else:
                reference[target-nums[x]] = x