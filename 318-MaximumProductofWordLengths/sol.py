class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ref = {}
        for word in words:
            marker = 0
            for c in set(word):
#                 this marks a specific location on a string of bit to 1
                marker |= (1 << (ord(c)-97))
            ref[marker] = max(ref.get(marker, 0), len(word))
#         not (x&y) means that the 2 words doesn't have same char
        return max([ref[x] * ref[y] for x in ref for y in ref if not (x & y)] or [0])