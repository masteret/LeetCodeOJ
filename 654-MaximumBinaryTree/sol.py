# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        max_val = -1
        index = -1
        for i, x in enumerate(nums):
            if x > max_val:
                max_val = x
                index = i
        result = TreeNode(max_val)
        result.left = self.constructMaximumBinaryTree(nums[:index])
        result.right = self.constructMaximumBinaryTree(nums[index+1:])
        return result