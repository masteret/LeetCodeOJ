class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [-1] * len(nums)
        # loop through the element twice
        loopy = range(len(nums))
        loopy = loopy + loopy
        for i in loopy:
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        return result
