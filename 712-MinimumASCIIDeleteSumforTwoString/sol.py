class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # DP solution
        i = len(s1)
        j = len(s2)
        # The cost for making s1.substring(i) and s2.substring(j) equal
        cost = [[0 for x in range(j+1)] for y in range(i+1)]
        # Base case is making s1.substring(i) equals to s2.substing(0)
        # and s1.substring(0) equals to s2.substring(i)
        for x in range(1, i+1):
            # works in ascii encode
            cost[x][0] = cost[x-1][0] + ord(s1[x-1])
        for x in range(1, j+1):
            cost[0][x] = cost[0][x-1] + ord(s2[x-1])
        for x in range(1, i+1):
            for y in range(1, j+1):
                if s1[x-1] == s2[y-1]:
                    # if both char are the same, cost is the same as sub1[:-1] and sub2[:-1]
                    cost[x][y] = cost[x-1][y-1]
                else:
                    # see removing which char has smaller cost
                    cost[x][y] = min(cost[x-1][y]+ord(s1[x-1]), cost[x][y-1]+ord(s2[y-1]))
        return cost[i][j]

a = Solution()
print a.minimumDeleteSum("sea", "eat")