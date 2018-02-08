class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        cur_g = cur_s = 0
        result = 0
        while cur_g < len(g) and cur_s < len(s):
            if g[cur_g] <= s[cur_s]:
                result += 1
                cur_s += 1
                cur_g += 1
            else:
                cur_s += 1
        return result