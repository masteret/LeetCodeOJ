class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        memorization/backtracking
        starts from smaller N
        memorize the result for possible number insert at that position (index starts at 1)
        eg. [1, [1]] - at 1st position, how many beautiful arrangment can I get using [1]

        """
        cache = {}
        def solve(ind, nums):
            # base case
            if len(nums) == 1:
                # There is a solution
                if nums[0] % ind == 0 or ind % nums[0] == 0:
                    cache[(ind, tuple(nums))] = 1
                    return 1
                # No solution
                else:
                    cache[(ind, tuple(nums))] = 0
                    return 0
            if (ind, tuple(nums)) in cache:
                return cache[(ind, tuple(nums))]
            total = 0
            for a, x in enumerate(nums):
                if x % ind == 0 or ind % x == 0:
                    # confirmed this position with this num can be used as part of beauti arrangment
                    # check to see if the remaining part is also beauti worthy
                    # at the end will reach len(nums) == 1 situation
                    # where we know if the whole chain is beauti or not
                    total += solve(ind+1, nums[:a] + nums[a+1:])
            cache[(ind, tuple(nums))] = total
            return total
        return solve(1, range(1, N+1))

a = Solution()
print a.countArrangement(2)