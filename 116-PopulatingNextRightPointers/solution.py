# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def recurse(self, node):
        if node is not None:
            if node.left is not None:
                node.left.next = node.right
                if node.next is not None:
                    node.right.next = node.next.left
                self.recurse(node.left)
                self.recurse(node.right)

    def connect(self, root):
        self.recurse(root)