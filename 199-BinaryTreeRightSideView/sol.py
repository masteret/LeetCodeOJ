# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, level):
        if node is None:
            return
        if level == len(self.result):
            self.result.append(node.val)

        if node.right is not None:
            self.helper(node.right, level+1)
        if node.left is not None:
            self.helper(node.left, level+1)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.helper(root, 0)
        return self.result