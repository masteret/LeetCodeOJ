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
    def find_next(self, node):
        """
            find the first occurence of child level node
        """
        if node is None:
            return None
        if node.left is not None:
            return node.left
        if node.right is not None:
            return node.right
        if node.next is not None:
            return self.find_next(node.next)
        return None

    def recurse(self, node):
        if node is not None:
            # both left and right nodes present
            if node.left is not None and node.right is not None:
                # connect left to right
                node.left.next = node.right
                # find the node for right to connect
                node.right.next = self.find_next(node.next)
                self.recurse(node.right)
                self.recurse(node.left)
            # only left present
            elif node.left is not None:
                node.left.next = self.find_next(node.next)
                self.recurse(node.left)
            # only right present
            elif node.right is not None:
                node.right.next = self.find_next(node.next)
                self.recurse(node.right)

    def connect(self, root):
        self.recurse(root)