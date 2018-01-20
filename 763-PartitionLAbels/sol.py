class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        tmp = []
        for x in S:
            for index, y in enumerate(tmp):
                if x in y:
                    tmp[index] = ''.join(tmp[index:]) + x
                    tmp = tmp[:index+1]
                    break
            else:
                tmp.append(x)
        return [len(x) for x in tmp]

a = Solution()
print a.partitionLabels("ababcbacadefegdehijhklij")
