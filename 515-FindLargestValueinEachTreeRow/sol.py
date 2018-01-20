# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.largest = {}

    def helper(self, node, level):
        if str(level) not in self.largest:
            self.largest[str(level)] = node.val
        else:
            self.largest[str(level)] = node.val if node.val > self.largest[str(level)] else self.largest[str(level)]
        if node.left is not None:
            self.helper(node.left, level+1)
        if node.right is not None:
            self.helper(node.right, level+1)

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.helper(root, 0)
        result = []
        for x in range(len(self.largest)):
            result.append(self.largest[str(x)])
        return result