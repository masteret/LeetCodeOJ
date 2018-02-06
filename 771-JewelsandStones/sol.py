class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0
        for x in J:
            tmp = S.count(x)
            if tmp > 0:
                result += tmp
        return result