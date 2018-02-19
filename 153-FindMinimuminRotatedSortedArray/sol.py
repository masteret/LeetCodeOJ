class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums)-1
        while lo < hi:
            # Case 1, left most < right most - list not rotated, can be skipped
            if nums[lo] < nums[hi]:
                return nums[lo]

            mid = (lo+hi)/2
            # case 2, mid element > right element, use right side of list
            if nums[mid] > nums[hi]:
                lo = mid+1
            else:
                # case 3, use left side of list
                hi = mid
        return nums[lo]

a = Solution()
print a.findMin([2,1])