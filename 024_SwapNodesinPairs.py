# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# 13% 56ms, interative, swap and connect neightbors in every odd node, then move next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prv = dummy
        cur = head
        while cur and cur.next:
            next_next = cur.next.next
            prv.next = cur.next
            cur.next.next = cur
            cur.next = next_next
            prv = cur
            cur = cur.next
            
        return dummy.next
        
# recursive
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head
