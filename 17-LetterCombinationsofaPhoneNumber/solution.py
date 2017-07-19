class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ref = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        }
        for key, val in ref.items():
            ref[key] = [x for x in val]
        prev = []
        now = []
        for x in digits:
            now = []
            if not prev:
                now = ref[x]
            else:
                for y in prev:
                    for z in ref[x]:
                        tmp = y + z
                        now.append(tmp)
            prev = now
        return now

a = Solution()
print a.letterCombinations("23")