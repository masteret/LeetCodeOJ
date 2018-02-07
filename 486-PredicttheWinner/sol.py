class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        score = [[0 for x in nums] for y in nums]
        for ind, x in enumerate(nums):
            score[ind][ind] = x
        # x is from left to right, we starts at [0][1], [1][2] down until [n-2][n-1] in first iteration of x
        for x in range(1, len(nums)):
            for y in range(len(nums)-x):
                # max of y decrease per iteration of x
                # which matches the number of score that needs to calucate in each iteration
                # as we move away from score[i][i], each iteration we calculate 1 less score

                # z is how far we move away from left to right
                z = x + y 
                # oponent will pick the max of remaining list, so use -
                score[y][z] = max(nums[y]-score[y+1][z], nums[z]-score[y][z-1])
        return score[0][-1] >= 0