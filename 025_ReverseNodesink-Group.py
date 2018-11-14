# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# 95% 56ms, traverse nodes and use stack to reverse nodes every k steps, time complexity O(n), space complexity O(k) 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        last = dummy
        cur = dummy.next
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next

            if len(stack) == k:
                while stack:
                    last.next = stack.pop()
                    last = last.next
                last.next = cur
            
        if stack:
            last.next = stack[0]
        return dummy.next
 
# not using stack
class Solution:

    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Dummy node initialization
        dummy = jump = ListNode(-1)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:
                count += 1
                r = r.next
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                jump.next = pre
                jump = l
                l = r
            else:
                return dummy.next
