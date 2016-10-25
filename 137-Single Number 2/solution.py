class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        found = {}
        for a in nums:
            if str(a) in found:
                del found[str(a)]
            else:
                found[str(a)] = 1

        if len(found) > 0:
            return int(found.keys()[0])

a = Solution()
print a.singleNumber([1,2,3,1,2,3,4])
print a.singleNumber([])