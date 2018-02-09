# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def __init__(self):
    #     import sys
    #     self.result = sys.maxint
    #     self.prev = None

    # def getMinimumDifference(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if root.left is not None:
    #         self.getMinimumDifference(root.left)

    #     if self.prev is not None:
    #         self.result = min(self.result, root.val - self.prev)
    #     self.prev = root.val

    #     if root.right is not None:
    #         self.getMinimumDifference(root.right)

    #     return self.result

    def helper(self, node):
        self.ele.append(node.val)
        if node.left is not None:
            self.helper(node.left)
        if node.right is not None:
            self.helper(node.right)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ele = []
        if root is not None:
            self.helper(root)
        self.ele = sorted(self.ele)
        import sys
        result = sys.maxint
        for x in range(len(self.ele)-1):
            result = min(result, abs(self.ele[x] - self.ele[x+1]))
        return result