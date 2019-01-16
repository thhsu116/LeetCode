# https://leetcode.com/problems/partition-list/

# 64ms 91%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = n1 = ListNode(0)  # partition whose nodes < x
        h2 = n2 = ListNode(0)  # partition whose nodes >= x
        node = head
        while node:
            #print(node.val)
            if node.val < x:
                n1.next = node
                n1 = n1.next
            else:
                n2.next = node
                n2 = n2.next
            node = node.next
        n2.next = None  # terminate new partitions since solution checker will iterate through all list nodes
        n1.next = h2.next
        return h1.next
