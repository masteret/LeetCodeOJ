# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        import itertools
        all_intervals = [y for x in schedule for y in x]
        sorted_time = sorted(all_intervals, key=lambda x: x.start)
        timeline = [sorted_time[0]]
        freetime = []
        for x in sorted_time[1:]:
            cur_time = timeline.pop()
            if x.start > cur_time.end:
                freetime.append(Interval(cur_time.end, x.start))
                timeline.append(x)
            else:
                if cur_time.end > x.end:
                    timeline.append(cur_time)
                else:
                    timeline.append(x)
        return freetime

a = Solution()
print a.employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]])