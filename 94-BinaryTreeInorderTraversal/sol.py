# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = []

    def helper(self, node):
        if node is not None:
            if node.left is not None:
                self.helper(node.left)
            self.result.append(node.val)
            if node.right is not None:
                self.helper(node.right)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.helper(root)
        return self.result