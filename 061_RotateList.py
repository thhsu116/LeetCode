# https://leetcode.com/problems/rotate-list/

# 44ms 99%, time complexity O(n), space complexity O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        if k == 0:
            return head
        
        node = head
        n = 1
        while node.next:
            node = node.next
            n += 1
        
        k = k % n
        
        if k == 0:
            return head
        else:
            node.next = head
            i = 1
            while i <= (n - k):
                node = node.next
                i += 1
            head = node.next
            node.next = None
            return head
