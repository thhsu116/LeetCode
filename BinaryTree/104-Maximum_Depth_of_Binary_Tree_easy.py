# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# "Bottom-up" Solution
class BUSolution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth)+1
 
# "Top-Down" Solution
class TDSolution:
    def maxDepth(self, root, d=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return d
        d += 1
        if not root.left and not root.right:
            return d
        left_depth = self.maxDepth(root.left, d)
        right_depth = self.maxDepth(root.right, d)
        return max(left_depth, right_depth)
