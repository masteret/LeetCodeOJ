class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return nums
        nums = sorted(nums)
        div_count = [1]*len(nums)
        div_pt = [-1]*len(nums)
        max_ind = 0
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if div_count[i] <= div_count[j]:
                        div_count[i] = div_count[j] + 1
                        div_pt[i] = j
            if div_count[i] > div_count[max_ind]:
                max_ind = i

        result = []
        while max_ind >= 0:
            result.append(nums[max_ind])
            max_ind = div_pt[max_ind]
        return result[::-1]

a = Solution()
print a.largestDivisibleSubset([1,2,3,4,9,12])
print a.largestDivisibleSubset([3,4,16,8])
