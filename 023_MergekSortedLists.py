# https://leetcode.com/submissions/detail/189056227/

# 13% 328ms, iterative, time complexity O(n*K), K = len(lists), space complexity O(1)
# approach 2 in solution,
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        vals = [l.val for l in lists if l]
        if not vals:
            return None
        dummy = ListNode(None)
        cur = dummy
        while vals:
            _min = min(vals)
            for i in range(len(lists)):
                if lists[i] and lists[i].val == _min:
                    cur.next = lists[i]
                    cur = lists[i]
                    lists[i] = lists[i].next
            vals = [l.val for l in lists if l]
        return dummy.next
        
# approace 3: optimize above with priority queue => reduce time complexity to O(n*logK)

# approach 5: devide and conquer by merging 2 sorted list at a time
