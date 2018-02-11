class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import collections
        task_counts = collections.Counter(tasks).values()
        biggest_task = max(task_counts)
        num_of_big_task = task_counts.count(biggest_task)
        return max(len(tasks), (biggest_task - 1) * (n + 1) + num_of_big_task)

a = Solution()
print a.leastInterval(["A","A","A","B","B","B"], 2)
print a.leastInterval(["A","B","C","A","B"], 2)