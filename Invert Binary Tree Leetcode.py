# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def flip(node):
            if node.left:
                if node.left.left or node.left.right:
                    flip(node.left)
            if node.right:
                if node.right.left or node.right.right:
                    flip(node.right)
            node.left, node.right= node.right, node.left
        if root and (root.left or root.right):
            flip(root)
        return root