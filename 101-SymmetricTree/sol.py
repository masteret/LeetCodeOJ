# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, left, right):
        if left is None and right is None:
            return
        if left.val != right.val:
            self.flag = False
            return
        if any([(left.left is None and right.right is not None),
                (left.left is not None and right.right is None),
                (left.right is None and right.left is not None),
                (left.right is not None and right.left is None)]):
            self.flag = False
            return
        if self.flag and left.left is not None and right.right is not None:
            self.helper(left.left, right.right)
        if self.flag and left.right is not None and right.left is not None:
            self.helper(left.right, right.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.flag = True
        self.helper(root, root)
        return self.flag