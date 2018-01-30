# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://en.wikipedia.org/wiki/Tree_traversal#Post-order
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = [(root, False)]  # use a flag to indicate whether the node has been visited or not.
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                ret.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return ret
