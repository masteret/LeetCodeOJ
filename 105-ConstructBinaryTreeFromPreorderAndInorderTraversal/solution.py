# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    master = None

    def helper(self, inord):
        if len(inord) == 0:
            return None
        if len(inord) == 1:
            self.master = self.master[1:]
            return TreeNode(inord[0])

        root = TreeNode(self.master[0])
        self.master = self.master[1:]
        root.left = self.helper(inord[:inord.index(root.val)])
        root.right = self.helper(inord[inord.index(root.val)+1:])
        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.master = preorder
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            self.master = self.master[1:]
            return TreeNode(inorder[0])

        root = TreeNode(self.master[0])
        self.master = self.master[1:]
        root.left = self.helper(inorder[:inorder.index(root.val)])
        root.right = self.helper(inorder[inorder.index(root.val)+1:])
        return root

a = Solution()
b = a.buildTree([1,2,3,4,5,6], [4,2,3,1,6,5])
import pdb
pdb.set_trace()
