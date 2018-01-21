# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.times = {}

    def helper(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            value = root.val
        elif root.left is not None and root.right is not None:
            value = root.val + self.helper(root.left) + self.helper(root.right)
        elif root.left is not None:
            value = root.val + self.helper(root.left)
        else:
            value = root.val + self.helper(root.right)


        if value in self.times:
            self.times[value] += 1
        else:
            self.times[value] = 1
        return value

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.helper(root)
        if self.times is None:
            return []
        max_occur = max(self.times.values())
        result = []
        for k, v in self.times.items():
            if v == max_occur:
                result.append(k)
        return result
