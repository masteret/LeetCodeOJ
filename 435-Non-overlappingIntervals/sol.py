# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x: x.end)
        cur_et = intervals[0].start
        count = 0
        for x in intervals:
            if x.start < cur_et:
                count += 1
            else:
                cur_et = x.end
            print count
        return count