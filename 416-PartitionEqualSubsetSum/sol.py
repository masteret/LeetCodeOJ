class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            # if not even, then it will never equal 0
            return False
        total /= 2

        result = [[False for x in range(total+1)] for y in range(len(nums)+1)]
        for x in range(len(nums)+1):
            result[x][0] = True

        for x in range(1, len(nums)+1):
            for y in range(1, total+1):
                if y >= nums[x-1]:
                    # array doesn't save negative sum value, so no need to calculate if y-nums[x-1] < 0
                    # result[x-1][y]: not picked current num x, its result depends on prevous result [x-1]
                    # result[x-1][y-nums[x-1]]: if picked current num x, it depends on previous result with a lesser sum
                    result[x][y] = result[x-1][y] | result[x-1][y-nums[x-1]]
                else:
                    result[x][y] = result[x-1][y]
        return result[-1][-1]
