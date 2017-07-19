class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num in findNums:
            ind = nums.index(num)
            value = 'unassigned'
            for subnum in nums[ind:]:
                if value == 'unassigned' and subnum > num:
                    value = subnum
            if value == 'unassigned':
                value = -1
            result.append(value)
        return result

a = Solution()
print a.nextGreaterElement([4,1,2], [1,3,4,2])
print a.nextGreaterElement([2,4], [1,2,3,4])