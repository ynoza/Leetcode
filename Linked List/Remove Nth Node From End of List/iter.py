# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow=head
        change=False
        fast=head
        while(fast):
            fast=fast.next
            if n<0:
                slow=slow.next
                change=True
            n-=1
        if n!=-1 and head and not change: return head.next
        elif slow and slow.next:
            slow.next=slow.next.next
        return head