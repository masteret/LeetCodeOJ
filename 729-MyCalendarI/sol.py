class MyCalendar:

    def __init__(self):
        self.interval = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s, e in self.interval:
            if not (start >= e or end <= s):
                return False
        self.interval.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)