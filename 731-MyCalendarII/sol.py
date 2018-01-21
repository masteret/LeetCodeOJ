class MyCalendarTwo:

    def __init__(self):
        self.all = []
        self.interval = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s, e in self.interval:
            if start < e and end > s:
                return False
        for s, e in self.all:
            if start < e and end > s:
                self.interval.append((max(s, start), min(e, end)))
        self.all.append((start, end))
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)