# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node):
        if node is None:
            return (0, 0)
        left_house = self.helper(node.left)
        right_house = self.helper(node.right)
        # if rob this house, both house under should be unrobbed
        rob_this = node.val+left_house[1]+right_house[1]
        # if not rob this house
        # it can be either both unrob, left unrob, right unrob and both rob
        both_not_rob = left_house[1] + right_house[1]
        left_not_rob = left_house[1] + right_house[0]
        right_not_rob = left_house[0] + right_house[1]
        both_rob = left_house[0] + right_house[0]
        not_rob = max([both_not_rob, left_not_rob, right_not_rob, both_rob])
        return rob_this, not_rob


    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rob_this, not_rob = self.helper(root)
        return max(rob_this, not_rob)