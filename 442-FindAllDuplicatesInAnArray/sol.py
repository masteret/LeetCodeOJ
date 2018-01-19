class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicate = []
        mark = {}
        for x in nums:
            if x in mark:
                duplicate.append(x)
            else:
                mark[x] = ""
        return duplicate