class Solution(object):
    def twoSum(self, nums, target):
        # build a 2 sum solver that generate non-duplicate result
        # left and right pointer points to value, if added up, append result
        # move pointers to next non-duplicate value
        # repeat 2 and 3
        # if doesn't add up, move left pt if smaller than target and move right pt if larger than target
        # output all result until l > r
        l = 0
        r = len(nums)-1
        result = []
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                # we found the target!
                result.append([nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
        return result
        

    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sorted the nums
        # for any num in nums that isn't duplicate with the previous one, do a 2 sums with the remaining list and target = -num
        # if there is a list of solution, propagate it with your current num
        result = []
        for i in range(len(nums)-2):
            if nums[i] == nums[i-1] and i > 0:
                continue
            tmp_result = self.twoSum(nums[i+1:], target-nums[i])
            if tmp_result != []:
                for x in tmp_result:
                    tmp = [nums[i]]
                    tmp.extend(x)
                    result.append(tmp)
        return result


    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        for i in range(len(nums)-3):
            if nums[i] == nums[i-1] and i > 0:
                continue
            tmp_result = self.threeSum(nums[i+1:], target-nums[i])
            if tmp_result != []:
                for x in tmp_result:
                    tmp = [nums[i]]
                    tmp.extend(x)
                    result.append(tmp)
        return result

a = Solution()
print a.fourSum([1, 0, -1, 0, -2, 2], 0)