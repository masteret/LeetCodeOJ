class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vert = 0
        hori = 0
        for x in moves:
            if x == "U":
                vert += 1
            elif x == "D":
                vert -= 1
            elif x == "L":
                hori -= 1
            elif x == "R":
                hori += 1
        if vert == hori == 0:
            return True
        return False