# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, a, b):
        if a is None and b is not None:
            return False
        if a is not None and b is None:
            return False
        if a is not None and b is not None:
            if a.val != b.val:
                return False
            return self.helper(a.left, b.left) and self.helper(a.right, b.right)
        return True
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.helper(p, q)
        