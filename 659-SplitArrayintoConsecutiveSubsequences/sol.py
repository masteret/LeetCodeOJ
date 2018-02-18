class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        freq = Counter(nums)
        end = {}
        for x in nums:
            if freq.get(x) == 0:
                continue
            if end.get(x-1, 0) > 0:
                end[x-1] -= 1
                end[x] = end.get(x, 0) + 1
                freq[x] -= 1
            elif freq.get(x+1, 0) > 0 and freq.get(x+2, 0) > 0:
                freq[x] -= 1
                freq[x+1] -= 1
                freq[x+2] -= 1
                end[x+2] = end.get(x+2, 0) + 1
            else:
                return False

        return True