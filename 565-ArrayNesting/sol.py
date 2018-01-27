class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # In this list, all element will eventually form a loop
        # so just need to mark all examined element into -1 when searching for longest loop
        def looping(index):
            count = 0
            while nums[index] >= 0:
                count += 1
                tmp = nums[index]
                nums[index] = -1
                index = tmp
            return count

        result = 0
        for x in range(len(nums)):
            if nums[x] >= 0:
                result = max(result, looping(x))
        return result

a = Solution()
print a.arrayNesting([5,4,0,3,1,6,2])