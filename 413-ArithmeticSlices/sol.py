class Solution(object):
    def isArith(self, nums):
        diff = nums[0]-nums[1]
        for x in range(len(nums)-1):
            if nums[x]-nums[x+1] != diff:
                return False
        return True

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        for x in range(len(A)-2):
            if self.isArith(A[x:x+3]):
                count += 1
                incr = 1
                while (x+3+incr <= len(A)) and self.isArith(A[x:x+3+incr]):
                    count += 1
                    incr += 1
        return count

a = Solution()
print a.numberOfArithmeticSlices([1,2,3,4])
print a.numberOfArithmeticSlices([1,2,3,8,9,10])