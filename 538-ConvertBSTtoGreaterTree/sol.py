# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.keys = []

    def key_helper(self, node):
        if node is not None:
            self.keys.append(node.val)
            if node.left is not None:
                self.key_helper(node.left)
            if node.right is not None:
                self.key_helper(node.right)

    def tree_builder(self, node):
        if node is not None:
            node.val = sum(self.keys[self.keys.index(node.val):])
            if node.left is not None:
                node.left = self.tree_builder(node.left)
            if node.right is not None:
                node.right = self.tree_builder(node.right)
        return node

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.key_helper(root)
        self.keys = sorted(self.keys)
        return self.tree_builder(root)