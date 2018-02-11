# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.data = []

    def helper(self, node):
        if node.left is not None:
            self.helper(node.left)
        self.data.append(node.val)
        if node.right is not None:
            self.helper(node.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.helper(root)
        return self.data[k-1]