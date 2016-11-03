class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        k = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                k.append(nums1[i])
                i += 1
            else:
                k.append(nums2[j])
                j += 1

        if i < len(nums1):
            k.extend(nums1[i:])

        if j < len(nums2):
            k.extend(nums2[j:])

        if (len(nums1) + len(nums2)) % 2 == 1:
            return float(k[(len(nums1) + len(nums2)) / 2])
        else:
            result = (float(k[(len(nums1) + len(nums2)) / 2]) + float(k[((len(nums1) + len(nums2)) / 2) - 1])) / 2
            return result

a =Solution()
print a.findMedianSortedArrays([1, 3], [2])
print a.findMedianSortedArrays([1, 2], [3, 4])

