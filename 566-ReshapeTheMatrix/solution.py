class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row_len = len(nums)
        col_len = len(nums[0])
        if row_len*col_len != r*c:
            return nums
        else:
            nums = iter([nums[i][j] for i in range(row_len) for j in range(col_len)])
            result = []
            print r, c
            for a in range(r):
                tmp = []
                for b in range(c):
                    tmp.append(nums.next())
                result.append(tmp)
            return result

a = Solution()
print a.matrixReshape([[1,2],[3,4]], 1, 4)
print a.matrixReshape([[1,2],[3,4]], 4, 1)
print a.matrixReshape([[1,2,3,4]], 2, 2)