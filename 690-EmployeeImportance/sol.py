"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def get_sum(self, emp_id):
        result = 0
        for x in self.data[emp_id].subordinates:
            result += self.get_sum(self.data[x].id)
        return result + self.data[emp_id].importance

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        self.data = {}
        for emp in employees:
            self.data[emp.id] = emp
        result = self.get_sum(id)
        return result