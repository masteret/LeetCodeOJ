class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        roots = set(dict)
        result = []
        for word in sentence.split():
            for i in range(len(word)):
                if word[:i] in roots:
                    result.append(word[:i])
                    break
            else:
                result.append(word)
        return " ".join(result)