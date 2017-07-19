class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        height = []
        for ppl in people:
            if not height:
                # if height is empty
                height.append(ppl)
            else:
                status = False
                for ind, val in enumerate(height):
                    # if the height of ppl is larger than the current person (val)
                    # insert ppl before current person
                    if ppl[0] > val[0]:
                        height.insert(ind, ppl)
                        status = True
                        break
                    # if height are the same for both person and ppl must stands in front of val
                    # insert ppl before current person
                    elif ppl[0] == val[0] and ppl[1] < val[1]:
                        height.insert(ind, ppl)
                        status = True
                        break
                # insert at the end
                if not status:
                    height.append(ppl)
        # @here we get a list that, tall person in front and short person at back
        # same height person with smaller see number in front
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        print height


        result = []
        for ppl in height:
            # insert each one based on there index
            result.insert(ppl[1], ppl)
        # [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        return result

a = Solution()
print a.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])