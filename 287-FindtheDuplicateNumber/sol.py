class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # meet in circle, hence 2 while loop
        # prove: https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.
        if len(nums) > 1:
            slow = nums[0]
            fast = nums[slow]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]

            fast = 0
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]

            return slow

        return -1