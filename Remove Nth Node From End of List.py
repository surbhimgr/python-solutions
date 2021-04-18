# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next==None and n==1:
            head=None
            return head
        prev=None
        slow=None
        fast=head
        cnt=1
        flag=True
        if n==1:
            while fast and fast.next:
                p=fast
                fast=fast.next
            p.next=None
            fast=None
            return head
        while fast and fast.next:
            fast=fast.next
            cnt+=1
            if cnt==n and flag==True:
                slow=head
                flag=False
                break
        while fast and fast.next:
            fast=fast.next
            prev=slow
            slow=slow.next
        if slow==head:
            head=head.next
            slow=None
        else:
            prev.next=slow.next
            slow=None
        return head
        
        