# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    depth = 0
    value = 0

    def helper(self, node, origin, depth):
        if node.left is None and node.right is None:
            if depth > self.depth:
                self.depth = depth
                self.value = node.val
        else:
            if node.left is not None:
                self.helper(node.left, "left", depth+1)
            if node.right is not None:
                self.helper(node.right, "right", depth+1)

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.value = root.val
        self.helper(root, "left", 0)
        return self.value