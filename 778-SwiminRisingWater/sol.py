class Solution(object):
    def canSwim(self, grid, level):
        actions = [(0, 0)]
        seen = set((0, 0))
        for x, y in actions:
            if grid[x][y] <= level:
                if x == y == len(grid)-1:
                    return True
                else:
                    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for m_x, m_y in moves:
                        new_x = x+m_x
                        new_y = y+m_y
                        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid) and (new_x, new_y) not in seen:
                            seen.add((new_x, new_y))
                            actions.append((new_x, new_y))
        return False

    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lo, hi = grid[0][0], len(grid)*len(grid)-1
        while lo < hi:
            cur = (lo + hi)/2
            if self.canSwim(grid, cur):
                hi = cur
            else:
                lo = cur+1
        return hi