# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# 72ms 99%, time O(n), space O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        new = head.next
        while new:
            if new.val != cur.val:
                cur.next = new
                cur = new
            else:
                cur.next = None
            new = new.next
        return head
