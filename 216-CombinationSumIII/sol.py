class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        import itertools
        # combs = itertools.combinations(range(1, 10), k)
        result = []
        for comb in itertools.combinations(range(1, 10), k):
            if sum(comb) == n:
                result.append(comb)
        return result