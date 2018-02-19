class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # import itertools
        # def is_asc(a):
        #     for x in range(1, len(a)):
        #         if a[x] < a[x-1]:
        #             return False
        #     return True
        # all_pos_comb = []
        # for x in range(2, len(nums)+1):
        #     all_pos_comb.extend(set(itertools.combinations(nums, x)))
        # return [x for x in all_pos_comb if is_asc(x)]

        subs = {()}
        for num in nums:
            subs |= {sub + (num,)
                     for sub in subs
                     if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]

a = Solution()
print a.findSubsequences([4, 6, 7, 7])