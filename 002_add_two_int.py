# https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 10% solution O(2n)
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_over = 0
        ret = []
        while l1 or l2:
            _sum = carry_over
            for l in [l1, l2]:
                if l:
                    _sum += l.val
            if _sum >=10:
                ret.append(_sum - 10)
                carry_over = 1
            else:
                ret.append(_sum)
                carry_over = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry_over:
            ret.append(1)
        for i in range(len(ret)-1, -1, -1):
            val = ret[i]
            ret[i] = ListNode(val)
            try:
                ret[i].next = ret[i+1]
            except:
                pass
            
        return ret[0]

# %69(116ms) solution
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """        
        num1 = 0
        num2 = 0
        loop_cnt = 0
        while True:
            if not l1 and not l2:
                break
            if l1:
                num1 += l1.val * 10**loop_cnt
                l1 = l1.next
            if l2:
                num2 += l2.val * 10**loop_cnt
                l2 = l2.next
            loop_cnt += 1
        _sum = num1 + num2
        prev_node = None
        curr_node = None
        for s in str(_sum):
            curr_node = ListNode(int(s))
            if prev_node:
                curr_node.next = prev_node
            prev_node = curr_node
        return curr_node
