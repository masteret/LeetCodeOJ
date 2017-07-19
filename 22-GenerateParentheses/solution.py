class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        else:
            result = []
            pre = self.generateParenthesis(n-1)
            for x in pre:
                tmp = '(' + x
                for index in range(1, len(tmp)):
                    subtmp = tmp[:index] + ")" + tmp[index:]
                    result.append(subtmp)
            result = list(set(result))
            return result

a = Solution()
print a.generateParenthesis(3)