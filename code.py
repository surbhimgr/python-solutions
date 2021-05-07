# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def func(node):
            head=node
            slow=node
            fast=node
            pre=None
            if fast==None:
                return None
            if fast.next==None:
                return TreeNode(fast.val)
            else:
                while fast and fast.next:
                    pre=slow
                    slow=slow.next
                    fast=fast.next.next
                root=TreeNode(slow.val)                
                pre.next=None
                root.left=func(head)
                root.right=func(slow.next)
                return root
        if head:
            root=func(head)
        else:
            return None
        return root