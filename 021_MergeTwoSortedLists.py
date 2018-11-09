# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 10% 76ms, traverse all nodes and save visited nodes to a list, then connect all nodes in list
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = [NodeList()]
        while l1 and l2:
            if l1.val > l2.val:
                ans.append(l2)
                l2 = l2.next
            elif l1.val < l2.val:
                ans.append(l1)
                l1 = l1.next
            else:
                ans.append(l1)
                ans.append(l2)
                l1, l2 = l1.next, l2.next
        while l1:
            ans.append(l1)
            l1 = l1.next
        while l2:
            ans.append(l2)
            l2 = l2.next
        for i in range(len(ans)-1):
            ans[i].next = ans[i+1]
        if ans:
            return ans[0] 
        else:
            return ans
            
# 40% 56ms, traverse all nodes, create new node and point previous created node to new node
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        node = dummy
        while l1 and l2:
            if l1.val > l2.val:
                node.next = ListNode(l2.val)
                l2 = l2.next
            elif l1.val < l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l1.val)
                node = node.next
                node.next = ListNode(l2.val)
                l1, l2 = l1.next, l2.next
            node = node.next
        if l1:
            node.next = l1
        if l2:
            node.next = l2

        return dummy.next
        
# 100% 40ms, don't create new node
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        node = dummy
        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            elif l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            node = node.next
        if l1:
            node.next = l1
        if l2:
            node.next = l2

        return dummy.next
