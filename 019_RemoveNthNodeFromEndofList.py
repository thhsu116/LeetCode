# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# 60% 44ms, use pass all nodes once and save passed node to a stack, then pop stack n times
# time complexity O(n), space complexity O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
            
        del_node = ''
        for _ in range(n):
            del_node = stack.pop()
        if stack:
            stack[-1].next = del_node.next
            return stack[0]
        else:
            return del_node.next
            
# try one pass solution with two pointers, time complexity O(n), space complexity O(1)
