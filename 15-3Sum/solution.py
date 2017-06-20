class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return False
        reference = {}
        for x in range(len(nums)):
            if nums[x] in reference:
                return [reference[nums[x]], x]
            else:
                reference[target-nums[x]] = x

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return False
        reference = {}
        result = []
        for x in range(len(nums)):
            tmp = list(nums)
            num = tmp.pop(x)
            if num in reference:
                result.append([x, reference[num][0], reference[num][1]])
            else:
                value = self.twoSum(tmp, 0)
                if value is not None:
                    reference[value[0]+value[1]] = [tmp[value[0]], value[1]]
        return result

a = Solution()
print a.threeSum([-1, 0, 1, 2, -1, -4])