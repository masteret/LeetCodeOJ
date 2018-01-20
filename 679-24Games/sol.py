class Solution(object):
    def __init__(self):
        self.status = False

    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if self.status:
            return self.status

        import itertools, math
        if len(nums) == 1:
            if 23.9 < nums[0] < 24.1:
                self.status = True
                return True
        else:
            for comb in itertools.permutations(nums):
                a = comb[0]
                b = comb[1]
                other = list(comb[2:])
                operations = [[a+b,], [a-b], [a*b], [b and float(a)/b]]
                operations = [x + other for x in operations]
                for next_step in operations:
                    if self.judgePoint24(next_step):
                        return True

        return self.status

a = Solution()
print(a.judgePoint24([4,1,8,7]))