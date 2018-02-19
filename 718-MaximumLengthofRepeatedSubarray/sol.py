class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for x in range(len(B)+1)] for y in range(len(A)+1)]
        for x in range(1, len(A)+1):
            for y in range(1, len(B)+1):
                if A[x-1] == B[y-1]:
                    dp[x][y] = dp[x-1][y-1]+1
        return max([max(x) for x in dp])