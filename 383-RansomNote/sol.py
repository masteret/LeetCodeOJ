class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        ransom = Counter(a for a in ransomNote)
        mag = Counter(b for b in magazine)
        ransom.subtract(mag)
        for char, count in ransom.most_common():
            if count > 0:
                return False
        return True