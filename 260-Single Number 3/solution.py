class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for a in nums:
            xor ^= a

        xor &= -xor

        result = [0, 0]
        for a in nums:
            if (a & xor) == 0:
                result[0] ^= a
            else:
                result[1] ^= a

        if result != [0, 0]:
            return result

a = Solution()
print a.singleNumber([1,2,3,1,2,3,4,5])
print a.singleNumber([])