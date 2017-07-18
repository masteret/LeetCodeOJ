class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        value = []
        for x in grid:
            tmp = []
            for y in x:
                tmp.append(5)
            value.append(tmp)

        for row, x in enumerate(grid):
            for col, y in enumerate(x):
                if y == 1:
                    value[row][col] -= 1
                    if col+1 < len(grid[0]) and grid[row][col+1] == 1:
                        value[row][col+1] -= 1
                        value[row][col] -= 1
                    if row+1 < len(grid) and grid[row+1][col] == 1:
                        value[row+1][col] -= 1
                        value[row][col] -= 1
        result = 0
        for x in value:
            for y in x:
                if y != 5:
                    result += y
        return result


a = Solution()
print a.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]])

print a.islandPerimeter([[]])