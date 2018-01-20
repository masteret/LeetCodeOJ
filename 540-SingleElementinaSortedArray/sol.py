class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for ind, x in enumerate(nums):
            if ind % 2 == 0:
                result -= x
            else:
                result += x
        return abs(result)

a = Solution()
print a.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print a.singleNonDuplicate([3,3,7,7,10,11,11])
