class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # total = 0
        # for i in range(32):
        #     count = 0
        #     for j in nums:
        #         if (j & pow(2, i)) != 0:
        #             count += 1
        #     total += count * (len(nums) - count)
        # return total
        # 1. generate a 32bit str for int
        # 2. for each num put their nth index bit into a tuple, generate 32 tuples
        # 3. count how many 0 and 1 in each tuple, multiply the number
        return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))

a = Solution()
print a.totalHammingDistance([1, 4])
print a.totalHammingDistance([4, 14, 2])