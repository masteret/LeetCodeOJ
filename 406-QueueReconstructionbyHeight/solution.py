class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        height = []
        for ppl in people:
            if not height:
                height.append(ppl)
            else:
                status = False
                for ind, val in enumerate(height):
                    if ppl[0] > val[0]:
                        height.insert(ind, ppl)
                        status = True
                        break
                    elif ppl[0] == val[0] and ppl[1] < val[1]:
                        height.insert(ind, ppl)
                        status = True
                        break
                if not status:
                    height.append(ppl)
        print height

        result = []
        for ppl in height:
            result.insert(ppl[1], ppl)
        return result

a = Solution()
print a.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])