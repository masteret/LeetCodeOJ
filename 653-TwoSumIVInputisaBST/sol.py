# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.reference = {}
        self.result = False

    def helper(self, node):
        if node.val in self.reference:
            self.result = True
            return True
        else:
            self.reference[self.k - node.val] = 1
            if not self.result and node.left is not None:
                self.helper(node.left)
            if not self.result and node.right is not None:
                self.helper(node.right)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.k = k
        if root is None:
            return False
        self.helper(root)
        return self.result