# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# BFS
# inpput can be []!!!
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        ret = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if level:
                ret.append(level)
        return ret
