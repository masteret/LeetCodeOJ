class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        for word in words:
            for row in rows:
                if all([x in row for x in word.lower()]):
                    result.append(word)
                    continue
        return result

a = Solution()
print a.findWords(["Hello", "Alaska", "Dad", "Peace"])