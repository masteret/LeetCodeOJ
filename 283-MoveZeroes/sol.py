class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_of_zero = nums.count(0)
        ind = 0
        while ind < len(nums)-num_of_zero:
            if nums[ind] == 0:
                nums.pop(ind)
                nums.append(0)
            else:
                ind += 1