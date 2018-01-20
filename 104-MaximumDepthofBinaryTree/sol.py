# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = 0

    def helper(self, node, level):
        if node.left is not None:
            self.helper(node.left, level+1)
        if node.right is not None:
            self.helper(node.right, level+1)
        if level > self.result:
            self.result = level

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root, 1)
        return self.result