class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in range(32):
            count = 0
            for j in nums:
                if (j & pow(2, i)) != 0:
                    count += 1
            total += count * (len(nums) - count)
        return total

a = Solution()
print a.totalHammingDistance([1, 4])
print a.totalHammingDistance([4, 14, 2])