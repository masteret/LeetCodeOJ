class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        lo, hi = 0, len(letters)
        while lo < hi:
            mid = (lo + hi)/2
            if ord(letters[mid]) > ord(target):
                hi = mid
            else:
                lo = mid+1
        return letters[lo%len(letters)]
