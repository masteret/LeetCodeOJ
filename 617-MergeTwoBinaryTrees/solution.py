# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is not None and t2 is not None:
            c = TreeNode(t1.val + t2.val)
        elif t1 is not None:
            return t1
        elif t2 is not None:
            return t2
        else:
            return None

        if t1.left is not None and t2.left is not None:
            c.left = self.mergeTrees(t1.left, t2.left)
        elif t1.left is not None and t2.left is None:
            c.left = t1.left
        elif t1.left is None and t2.left is not None:
            c.left = t2.left
        else:
            c.left = None

        if t1.right is not None and t2.right is not None:
            c.right = self.mergeTrees(t1.right, t2.right)
        elif t1.right is not None and t2.right is None:
            c.right = t1.right
        elif t1.right is None and t2.right is not None:
            c.right = t2.right
        else:
            c.right = None
        return c

if __name__ == "__main__":
    a = TreeNode(1)
    a.left = TreeNode(3)
    a.right = TreeNode(2)
    a.left.left = TreeNode(5)

    b = TreeNode(2)
    b.left = TreeNode(1)
    b.left.right = TreeNode(4)
    b.right = TreeNode(3)
    b.right.right = TreeNode(7)

    c = Solution()
    d = c.mergeTrees(a, b)
    import pdb
    pdb.set_trace()