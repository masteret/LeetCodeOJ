class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        if len(nums1) < len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
        result = []
        for x in nums2:
            if x in nums1:
                nums1.remove(x)
                result.append(x)
        return result

a = Solution()
print a.intersect([1, 2], [1, 1])