# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, sofar):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.result.append('->'.join(sofar+[str(node.val)]))
            return
        if node.left is not None:
            self.helper(node.left, sofar+[str(node.val)])
        if node.right is not None:
            self.helper(node.right, sofar+[str(node.val)])

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        self.helper(root, [])
        return self.result