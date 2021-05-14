# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        def flat(root):
            if root==None or root.left==None and root.right==None:
                return
            if root.left!=None:
                flat(root.left)
                tmp=root.right
                root.right=root.left
                root.left=None
                t=root.right
                while t.right!=None:
                    t=t.right
                t.right=tmp
            flat(root.right)
        flat(root)
