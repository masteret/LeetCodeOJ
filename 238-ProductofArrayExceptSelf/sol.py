class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # This is a math trick...
        # scan forward once, muliply each value
        # scan backward once, muliply each value and use it to multiply with the previous scan
        tmp = 1
        result = [1]
        for ind, x in enumerate(nums[:-1]):
            tmp *= x
            result.append(tmp)
        tmp = 1
        for ind, x in enumerate(nums[:0:-1]):
            tmp *= x
            result[-ind-2] *= tmp
        return result

a = Solution()
print a.productExceptSelf([0, 0])
print a.productExceptSelf([1,2,3,4])