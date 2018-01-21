class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for x in nums:
            if nums[abs(x)-1] > 0:
                nums[abs(x)-1] = -nums[abs(x)-1]
        result = []
        for x in range(len(nums)):
            if nums[x] > 0:
                result.append(x+1)
        return result