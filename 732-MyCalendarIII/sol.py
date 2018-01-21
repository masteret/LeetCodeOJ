class MyCalendarThree(object):

    def __init__(self):
        self.intervals = {}
        self.sorted_time = []
        self.max_val = 0     

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        # if it is a start time, increase the count by 1
        # if it is an end time, decrease it by 1
        # that way when travelling through the interval, at any point
        # the count number indicates how many intervals are we currently on
        self.intervals[start] = self.intervals.get(start, 0)+1
        self.intervals[end] = self.intervals.get(end, 0)-1

        import bisect
        # get the index of where to insert start into sorted_time
        s = bisect.bisect_left(self.sorted_time, start)
        # only in 3 situations we will insert the start time
        # 1. sorted_time list is empty
        # 2. inserting at the end
        # 3. the index that we are inserting doesn't have the same value
        # e.g. no need to mark a 10s start time for 2 intervals in the sorted_time list
        # since the 2 intervals are being tracked by intervals already
        if not self.sorted_time or s >= len(self.sorted_time) or self.sorted_time[s] != start:
            bisect.insort_left(self.sorted_time, start)

        e = bisect.bisect_left(self.sorted_time, end)
        if not self.sorted_time or e >= len(self.sorted_time) or self.sorted_time[e] != end:
            bisect.insort_left(self.sorted_time, end)

        count = 0
        for key in self.sorted_time:
            count += self.intervals[key]
            self.max_val = max(self.max_val, count)

        return self.max_val



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)