class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.magic = {}
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            for x in range(len(word)):
                cur = word[:x]+"*"+word[x+1:]
                if cur in self.magic and word not in self.magic[cur]:
                    self.magic[cur].append(word)
                elif cur not in self.magic:
                    self.magic[cur] = [word]

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for x in range(len(word)):
            cur = word[:x]+"*"+word[x+1:]
            if cur in self.magic:
                magicwords = self.magic[cur]
                if len(magicwords) == 1 and word != magicwords[0]:
                    return True
                elif len(magicwords) > 1:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)