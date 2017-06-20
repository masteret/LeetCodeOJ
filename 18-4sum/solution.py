class Solution(object):
    def helper(self, nums, target, count):
        if count == 1:
            result = []
            for i in nums:
                if i == target:
                    result.append([i])
            return result
        else:
            result = []
            for i in range(len(nums)):
                tmp_nums = list(nums)
                tmp_value = tmp_nums.pop(i)
                tmp_target = target - tmp_value
                tmp_result = self.helper(tmp_nums, tmp_target, count-1)
                # print "****************************"
                # print nums, target, count
                # print tmp_nums, tmp_target, count-1
                # print tmp_result
                for inner in tmp_result:
                    tmp_list = [tmp_value]
                    if None not in inner:
                        tmp_list.extend(inner)
                        result.append(tmp_list)
            return result


    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return [list(y) for y in set(tuple(sorted(x)) for x in self.helper(nums, target, 4))]

a = Solution()
print a.fourSum([1, 0, -1, 0, -2, 2], 0)