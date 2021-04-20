"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        def opennode(node,ans):
            if node!=None:
                ans.append(node.val)
                if node.children:
                    for c in node.children:
                        opennode(c,ans)
        opennode(root,ans)
        return ans