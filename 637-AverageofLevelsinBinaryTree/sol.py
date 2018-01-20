# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.count = {}
        self.values = {}

    def helper(self, node, level):
        if level in self.values:
            self.values[level] += node.val
            self.count[level] += 1
        else:
            self.values[level] = node.val
            self.count[level] = 1
        if node.left is not None:
            self.helper(node.left, level+1)
        if node.right is not None:
            self.helper(node.right, level+1)

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.helper(root, 0)
        result = []
        for key in range(len(self.count.keys())):
            result.append(float(self.values[key])/self.count[key])
        return result

