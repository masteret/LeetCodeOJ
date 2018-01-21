class Solution(object):
    def findArea(self, grid, r, c, area):
        if not self.checked[r][c]:
            self.checked[r][c] = 1
            area += 1
            if r+1 < len(grid) and grid[r+1][c]:
                area = self.findArea(grid, r+1, c, area)
            if c+1 < len(grid[0]) and grid[r][c+1]:
                area = self.findArea(grid, r, c+1, area)

            if r-1 >= 0 and grid[r-1][c]:
                area = self.findArea(grid, r-1, c, area)
            if c-1 >= 0 and grid[r][c-1]:
                area = self.findArea(grid, r, c-1, area)

        return area

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid and grid[0]:
            self.checked = [[0 for x in grid[0]] for y in grid]
        else:
            self.checked = []

        max_area = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val and not self.checked[r][c]:
                    max_area = max(self.findArea(grid, r, c, 0), max_area)
        return max_area

a = Solution()
print a.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
print a.maxAreaOfIsland([[0,1],[1,1]])