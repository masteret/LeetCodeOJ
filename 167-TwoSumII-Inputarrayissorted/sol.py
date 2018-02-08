class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = 0
        t = len(numbers)-1
        while s < t:
            if numbers[s]+numbers[t] == target:
                return [s+1, t+1]
            elif numbers[s]+numbers[t] > target:
                t -= 1
            else:
                s += 1
        return []