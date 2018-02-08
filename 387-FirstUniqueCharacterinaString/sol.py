class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(s)
        unique = [x[0] for x in cnt.most_common() if x[1] == 1]
        return min([s.index(x) for x in unique] or [-1])        
