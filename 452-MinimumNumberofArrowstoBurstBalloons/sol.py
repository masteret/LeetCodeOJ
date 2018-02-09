class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        import sys
        points = sorted(points, key=lambda x: x[1])
        result = 0
        # aim 1st arrow at the left most of the screen
        cur_arrow = -sys.maxint-1
        for bal in points:
            if bal[0] > cur_arrow:
                result += 1
                cur_arrow = bal[1]
        return result