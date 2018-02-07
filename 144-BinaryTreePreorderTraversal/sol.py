# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop(0)
            result.append(node.val)
            if node.right is not None:
                stack.insert(0, node.right)
            if node.left is not None:
                stack.insert(0, node.left)
        return result