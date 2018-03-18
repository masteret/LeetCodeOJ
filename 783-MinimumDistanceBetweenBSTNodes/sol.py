# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root.left is not None:
            self.helper(root.left)
        self.l.append(root.val)
        if root.right is not None:
            self.helper(root.right)

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.l = []
        self.helper(root)
        ans = 2**32
        for x in range(len(self.l)-1):
            ans = min(ans, abs(self.l[x]-self.l[x+1]))
        return ans