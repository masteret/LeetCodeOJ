class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code
        # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85193/Binary-Search-Heap-and-Sorting-comparison-with-concise-code-and-1-liners-Python-72-ms
        import bisect
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi)//2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid+1
            else:
                hi = mid
        return lo