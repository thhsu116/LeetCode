# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''execute the following recursively:
   1. last node in postorder is top node of the subtree
   2. inorder is [left trr nodes, top node, right tree nodes]
   3. postorder is [left tree nodes, right tree nodes, top node]
   4. break inorder and postorder into left tree and right tree
'''
class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return
        top = TreeNode(postorder.pop())
        i = inorder.index(top.val)
        inorder_left = inorder[:i]
        inorder_right = inorder[i+1:]
        postorder_left = postorder[:i]
        postorder_right = postorder[i:]
        top.left = self.buildTree(inorder_left, postorder_left)
        top.right = self.buildTree(inorder_right, postorder_right)
        return top
