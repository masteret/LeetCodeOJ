class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        found = {}
        for a in nums:
            if str(a) in found:
                found[str(a)] += 1
            else:
                found[str(a)] = 1

        for key, val in found.items():
            if val == 1:
                return int(key)

a = Solution()
print a.singleNumber([1,2,3,1,2,3,4])
print a.singleNumber([])