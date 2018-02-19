# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        import bisect
        ref = sorted([(v.start, i) for i, v in enumerate(intervals)])
        result = []
        for x in intervals:
            ind = bisect.bisect_left(ref, (x.end, ))
            if ind != len(intervals):
                result.append(ref[ind][1])
            else:
                result.append(-1)
        return result