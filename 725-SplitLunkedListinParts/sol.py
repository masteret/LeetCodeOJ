# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        lengy = 0
        node = root
        while node != None:
            lengy += 1
            node = node.next

        reg_size = lengy/k
        larger = lengy%k
        result = []
        node = root
        for x in range(larger):
            tmp = []
            for y in range(reg_size+1):
                tmp.append(node.val)
                node = node.next
            result.append(tmp)
        for x in range(k-larger):
            tmp = []
            for y in range(reg_size):
                tmp.append(node.val)
                node = node.next
            result.append(tmp)
        return result