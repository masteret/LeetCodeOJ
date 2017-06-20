class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sums = sum([nums[i] for i in range(0, len(nums), 2)])
        return sums

a = Solution()
print a.arrayPairSum([1,2,3,4])