# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        stack = [root]
        while stack:
            num_nodes = len(stack)
            for i in range(num_nodes):
                node = stack.pop(0)
                if node:
                    if i+1 < num_nodes:
                        node.next = stack[0]
                    if node.left: stack.append(node.left)
                    if node.right: stack.append(node.right)
    # iterative, O(1) space
    def connect2(self, root):
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next

node1 = TreeLinkNode(1)
node2 = TreeLinkNode(2)
node3 = TreeLinkNode(3)
node1.left = node2
node1.right = node3
