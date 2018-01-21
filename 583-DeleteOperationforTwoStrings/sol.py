class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # look for 712 to see what's behind this
        i = len(word1)
        j = len(word2)
        length = max(i, j)
        cost = [[0 for x in range(length+1)] for y in range(length+1)]
        for x in range(1, i+1):
            cost[x][0] = x
        for y in range(1, j+1):
            cost[0][y] = y
        for x in range(1, i+1):
            for y in range(1, j+1):
                if word1[x-1] == word2[y-1]:
                    cost[x][y] = cost[x-1][y-1]
                else:
                    cost[x][y] = min(cost[x-1][y], cost[x][y-1]) + 1
        return cost[i][j]

a = Solution()
print a.minDistance("a", "ab")