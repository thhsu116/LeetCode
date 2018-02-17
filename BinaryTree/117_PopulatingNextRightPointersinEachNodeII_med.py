# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37828/O(1)-space-O(n)-complexity-Iterative-Solution
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        head=root  # The left most node in the lower level
        prev=None  # The previous node in the lower level
        curr=None  # The current node in the upper level
        while head:
            curr=head
            prev=None
            head=None
            while curr:
                if curr.left:
                    if prev:
                        prev.next=curr.left
                    else:
                        head=curr.left
                    prev=curr.left
                if curr.right:
                    if prev:
                        prev.next=curr.right
                    else:
                        head=curr.right
                    prev=curr.right
                curr=curr.next
